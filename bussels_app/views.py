from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import hashers
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.db.models import Avg, Sum, Max, Count
from django.utils import dateformat
from saturdays_list import past_saturdays
from info_system.views import *
from models import *
from forms import *
import datetime
import calendar

# This view shows all available bussels in our DB

class BusselListView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "bussels_app/bussel_list.html"
    login_url ="/login/"
    group_required= [u"Bussell", u"Manager"]
    raise_exception = show_access_denied_page

class BusselDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    template_name ="bussels_app/bussel_detail.html"
    model = Bussel
    login_url ="/login/"
    group_required= [u"Bussell", u"Manager"]
    raise_exception = show_access_denied_page

    # add the attendance and average data to the context
    def get_context_data(self, **kwargs):
        context = super(BusselDetailView, self).get_context_data(**kwargs)
        bussel = []
        church = []
        souls = []
        offertory = []
        offertory_per_head = []

        # try getting all reports for this Bussel
        try:
            bussel_reports = BusselReport.objects.filter(bussel=self.get_object()) 
            latest_report = bussel_reports.latest()

        # No report at all exist within the database for this bussel
        except BusselReport.DoesNotExist:
            print "Report not Found"
            bussel = [0]*12
            church = [0]*12
            souls = [0]*12
            offertory = [0]*12
            offertory_per_head = [0]*12

            attendance_data = {'bussel': bussel,
                           'church': church,
                           'souls': souls, 
                           'offertory': offertory,
                           'offertory_per_head': offertory_per_head
                           }
            context["attendance_data"]  = attendance_data
            context["chart_label"]  = [rev for rev in reversed([saturday.strftime('%d-%m-%Y') \
                                                                for saturday in past_saturdays(12)])]
            context["latest_offertory"] = 0 
            context["average_offertory"] = 0

            context["average_bussel_attendance"] = 0 
            context["average_church_attendance"] = 0 
            context["average_souls_won"] = 0 
            return context

        for saturday in reversed([day for day in past_saturdays(12)]):
            # try getting a report for the said date
            try:
                report = bussel_reports.get(date=saturday)
            # No report exists for the said date
            except BusselReport.DoesNotExist:
                bussel.append(0)
                church.append(0)
                souls.append(0)
                offertory.append(0.0)
                offertory_per_head.append(0.0)
                print "nothing to report"
                continue
            bussel.append(report.bussel_attendance)
            church.append(report.church_attendance)
            souls.append(report.num_souls_won)
            offertory.append(report.offertory_given)
            offertory_per_head.append(report.offertory_given/report.bussel_attendance)

        attendance_data = {'bussel': bussel,
                           'church': church,
                           'souls': souls, 
                           'offertory': offertory,
                           'offertory_per_head': offertory_per_head,
                           }
        context["attendance_data"]  = attendance_data
        context["chart_label"]  = [rev for rev in reversed([saturday.strftime('%d-%m-%Y') \
                                                            for saturday in past_saturdays(12)])]
        context["average_offertory"] = bussel_reports.aggregate(Avg("offertory_given"))
        context["average_offertory_per_head"] = bussel_reports.aggregate(Avg("offertory_given")).values()[0]\
                              /bussel_reports.aggregate(Avg("bussel_attendance")).values()[0]

        context["average_bussel_attendance"] = bussel_reports.aggregate(Avg("bussel_attendance"))
        context["average_church_attendance"] = bussel_reports.aggregate(Avg("church_attendance"))
        context["average_souls_won"] = bussel_reports.aggregate(Avg("num_souls_won"))
        context["longitude"] = self.get_object().bussel_location['coordinates'][0] 
        context["latitude"] = self.get_object().bussel_location['coordinates'][1] 
        return context

class SectionUnderDevelopment(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "bussels_app/under_development.html"
    group_required= [u"Bussell", u"Manager", u"Finance"]
    login_url = "/login/"
    raise_exception = show_access_denied_page

class AccessDenied(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "bussels_app/access_denied.html"

def authenticate_bussel(bussel_code, bussel_password):
    # let's see if a bussel exists with this code
    try:
        bussel = Bussel.objects.get(code=bussel_code)
        print bussel
        print bussel_password
        print hashers.check_password(bussel_password, bussel.password) 
        return hashers.check_password(bussel_password, bussel.password) 

    except Bussel.DoesNotExist:
        "No bussel found"
        return False

def authenticate_bussel_request(request):
    code = request.GET["code"]
    password = request.GET["password"]

    if authenticate_bussel(code, password):
        bussell = Bussel.objects.get(code=code)
        return JsonResponse({"bussell_id":bussell.id, "bussell_name":bussell.name, "bussell_profile":bussell.group_pic},
                            safe=False, status=200)
        #return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)

@csrf_exempt
def change_bussel_password(request):
    code = request.POST["code"]
    old_password = request.POST["old_password"]

    if not authenticate_bussel(code, old_password):
        return HttpResponse(status=401)
    else:
        new_password_one = request.POST["new_password_one"]
        new_password_two = request.POST["new_password_two"]

        if new_password_one == new_password_two:
            bussel = Bussel.objects.get(code=code)
            bussel.password = new_password_one
            bussel.save()
            return HttpResponse(status=200)

        else:
            return HttpResponse(status=400)

def change_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', { 
        'form': form
    })

@csrf_exempt
def update_bussell_profile(request):
    pid = request.POST["bussell_id"]
    profile_url = request.POST["profile"]
    bussell = Bussel.objects.get(pk=pid)
    bussell.group_pic = profile_url
    bussell.save()
    return HttpResponse(status=200)

@csrf_exempt   
def get_bussell_group_pic_url(request):
    pid = request.POST["bussell_id"]
    bussell = Bussel.objects.get(pk=pid)
    return JsonResponse({"profile_url":bussell.group_pic}, status=200, safe=False)

def update_bussel_location(request):
    code = request.GET["code"]
    lat  = request.GET["lat"]
    lon  = request.GET["lon"]

    bussel = Bussel.objects.get(code=code)

    bussel.bussel_location = {'type':'Point', 'coordinates': [float(lon), float(lat)]}

    bussel.save()

    return HttpResponse(status=200)


def json_bussel_list(request):
    
    if request.method == "GET":
        bussels = Bussel.objects.filter(status=1)
        object_list = []

        for bussel in bussels:
            object_dict = {}
            object_dict['pk'] = bussel.pk
            object_dict['name'] = bussel.name
            object_dict['code'] = bussel.code
            object_dict['leader'] = bussel.leader.first_name + " " + \
                bussel.leader.middle_name + " " + bussel.leader.last_name
            object_dict['leader_short'] = bussel.leader.first_name + " " + \
                 bussel.leader.last_name
            object_dict['location'] = "HNo. " + bussel.house_number + ", " + \
                bussel.street_name+ ", " + bussel.suburb
            object_dict['location_short'] = bussel.suburb
            object_list.append(object_dict)

        return JsonResponse(object_list, safe=False)

# get all bussel reports for the given date
class BusselReportListView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "bussels_app/bussel_reports_list.html"
    login_url ="/login/"
    group_required= [u"Bussell", u"Manager"]
    raise_exception = show_access_denied_page

    def get_context_data(self, **kwargs):
        context = super(BusselReportListView, self).get_context_data(**kwargs)
        context["saturdays"] = past_saturdays(12)
        return context

class RequestDateWrapper:
    current_request_date = datetime.date.today()
    
    def set_request_date(self, date):
        self.current_request_date = date

    def get_request_date(self):
        return self.current_request_date

request_date_wrapper = RequestDateWrapper()

def json_bussel_reports_list(request):
    
    if request.method == "GET":
        request_date  = request.GET["request_date"]
        yr, mn, day   = request_date.split("-")
        request_date  = datetime.date(int(yr), int(mn), int(day))
        request_date_wrapper.set_request_date(request_date)
        try:
            bussel_reports = BusselReport.objects.filter(date=request_date)
        except BusselReport.DoesNotExist:
            return JsonResponse([], safe=False)
        print bussel_reports
        offertory_total = bussel_reports.aggregate(Sum('offertory_given'))
        souls_won_total = bussel_reports.aggregate(Sum('num_souls_won'))
        bussel_attendance_total = bussel_reports.aggregate(Sum('bussel_attendance'))
        church_attendance_total = bussel_reports.aggregate(Sum('church_attendance'))
        object_list = []

        for report in bussel_reports:
            object_dict = {}
            object_dict['pk'] = report.pk
            object_dict['name'] = report.bussel.name
            object_dict['leader'] = report.bussel.leader.first_name + " " + \
                report.bussel.leader.middle_name + " " + report.bussel.leader.last_name

            object_dict['leader_short'] = report.bussel.leader.first_name + " " + \
                report.bussel.leader.last_name
            object_dict['b_attendance'] = report.bussel_attendance
            object_dict['c_attendance'] = report.church_attendance
            object_dict['time'] = report.time.strftime('%H:%M:%S')
            object_dict['topic'] = report.topic
            object_dict['first_timers'] = report.num_first_timers
            object_dict['souls_won'] = report.num_souls_won
            object_dict['time_started'] = report.time_started
            object_dict['time_ended'] = report.time_ended
            object_dict['offertory'] = report.offertory_given

            object_dict.update(offertory_total)
            object_dict.update(souls_won_total)
            object_dict.update(bussel_attendance_total)
            object_dict.update(church_attendance_total)
            object_list.append(object_dict)

        return JsonResponse(object_list, safe=False)

def bussell_reports_header_json(request):

    report_headers = BusselReport.objects.all() \
        .extra({'mdate':"date(date)"}) \
        .values('date') \
        .annotate(count=Count('id')).order_by('-date')
    bussell_total = Bussel.objects.all().count()

    object_list = []
    for header in report_headers:
        object_dict = {}
        object_dict['date'] = dateformat.format(header.get('date'), 'U')
        object_dict['count'] = header.get('count')
        object_dict['total'] = bussell_total

        object_list.append(object_dict)

    return JsonResponse(object_list, safe=False)


class BusselReportEditView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = BusselReport
    form_class = BusselReportDetailForm
    template_name = "bussels_app/bussel_report_detail.html"
    login_url ="/login/"
    group_required= [u"Bussell", u"Manager"]
    raise_exception = show_access_denied_page

    def get_context_data(self, **kwargs):
        context = super(BusselReportEditView, self).get_context_data(**kwargs)
        from django.forms.models import model_to_dict
        report = BusselReport.objects.get(pk=kwargs['pk'])
        time_format = report.time.strftime("%H:%M:%S")
        my_dict = model_to_dict(report)
        my_dict["time"] = time_format
        bussel_report_form = BusselReportDetailForm(initial=my_dict)
        context["form"] = bussel_report_form
        context["bussel_name"] = report.bussel.name
        return context
    def get(self, request, *args, **kwargs):
        self.object = None
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        self.object = None
        form =  BusselReportDetailForm(request.POST)
        print form
        if form.is_valid():
            report = BusselReport.objects.get(pk=kwargs['pk'])
            report.topic = request.POST['topic']
            report.time_started = request.POST['time_started']
            report.time_ended = request.POST['time_ended']
            report.bussel_attendance = request.POST['bussel_attendance']
            report.church_attendance = request.POST['church_attendance']
            report.num_souls_won = request.POST['num_souls_won']
            report.num_first_timers = request.POST['num_first_timers']
            report.offertory_given = request.POST['offertory_given']
            report.save()
            return HttpResponseRedirect(reverse("bussel:all-bussel-reports")) 
        print form.errors
        return render(request, self.template_name, self.get_context_data(**kwargs))


# this view gets the report from the leaders android phone ---
# TODO
# report should be only for the current saturday all other dates should not be accepted.
# remove the freedom in choosing the date when code is running in production.
@csrf_exempt
def save_bussel_report(request):
    bussel_code = request.POST["code"]
    bussel_password = request.POST["password"]
    # successful authentication
    if authenticate_bussel(bussel_code, bussel_password):
        bussel = Bussel.objects.get(code=bussel_code)
        bussel_report_dates = BusselReport.objects.filter(bussel=bussel).values_list('date')
        report_date = datetime.date.today() 
        # An already submitted report
        if (report_date,) in bussel_report_dates:
            report = BusselReport.objects.get(bussel=bussel, date=report_date)
            report.topic=request.POST['topic']
            report.notes=request.POST['notes']
            report.time_started = request.POST['time_started']
            report.time_ended = request.POST['time_ended']
            report.bussel_attendance=request.POST['bussel_attendance']
            report.num_souls_won=request.POST['num_souls_won']
            report.num_first_timers=request.POST['num_first_timers']
            report.offertory_given=request.POST['offertory']
            report.save()

            if(request.POST.get("attendance_list", None) is not None):
                old_attendance = BussellMemberAttendance.objects.filter(bussell_report=report)
                # clear previous attendance data
                [attendance.delete() for attendance in old_attendance]
                attendance_list = eval(request.POST["attendance_list"])
                for pk in attendance_list:
                    attendance = BussellMemberAttendance.objects.create(
                        bussell_member = BussellMember.objects.get(pk=pk),
                        bussell_report = report,
                        bussell_attendance = True
                    )
                    attendance.save()
            return HttpResponse(status=200)

        # A report on a day other than Saturday
        # excuse us if we are debugging
        debug = eval(request.POST.get("debug", "False"))
        if (report_date.weekday() != 5) and not debug:
            print "Reporting Window Closed"
            return HttpResponse(status=403)

        report = BusselReport.objects.create(
                 topic=request.POST['topic'],
                 time_started = request.POST['time_started'],
                 time_ended = request.POST['time_ended'],
                 date = report_date,
                 notes = request.POST['notes'],
                 bussel_attendance=request.POST['bussel_attendance'],
                 num_souls_won=request.POST['num_souls_won'],
                 num_first_timers=request.POST['num_first_timers'],
                 offertory_given=request.POST['offertory'],
                 bussel=bussel
        )
        if(request.POST.get("attendance_list", None) is not None):
            attendance_list = eval(request.POST["attendance_list"])
            for pk in attendance_list:
                attendance = BussellMemberAttendance.objects.create(
                    bussell_member = BussellMember.objects.get(pk=pk),
                    bussell_report = report,
                    bussell_attendance = True
                )
                attendance.save()
        return HttpResponse(status=200)
    # Unsuccessful authentication
    else:
        return HttpResponse(status=401)

    
# this checks if a bussell report has any BussellMemberAttendance object
# attached to it. So that a button is provided in UI to view such list
def check_attendance_status(request):
    bussell_report_id = request.GET["report_id"]
    # get all available attendance for this bussell
    bussell_report = BusselReport.objects.get(pk=bussell_report_id)
    attendance_for_bussell = BussellMemberAttendance.objects.filter(bussell_report=bussell_report)
    
    editable = bussell_report.date == datetime.date.today()
    bussell_attendance_view = attendance_for_bussell.count()!=0
    
    deadline = datetime.datetime.combine(bussell_report.date, datetime.time(0,0,0)) + datetime.timedelta(hours=40)
    church_attendance_updatable = datetime.datetime.now()<deadline
    
    return JsonResponse({"editable": editable,
                          "b_attendance_view": bussell_attendance_view, 
                          "c_attendance_updatable": church_attendance_updatable},
                         safe=False, status=200)

def get_members_attendance_for_report(request):
    bussell_report_id = request.GET["report_id"]
    
    bussell_report = BusselReport.objects.get(pk=bussell_report_id)
    
    bussell_members = BussellMember.objects.filter(bussell=Bussel.objects.get(pk=bussell_report.bussel.pk))
    
    response_list = []
    for member in bussell_members:
        member_object = {}
        attendance_for_report = BussellMemberAttendance.objects.filter(bussell_report=bussell_report, bussell_member=member)
        attendance = attendance_for_report.first()
        
        member_object["id"] = member.pk
        member_object["first_name"] = member.first_name
        member_object["other_names"] = member.other_names
        member_object["phone"] = member.phone
        member_object["profile_pic"] = member.profile_pic
        member_object["is_church_member"] = member.church_member
        
        if attendance is not None:
            member_object["bussell_attendance"] = attendance.bussell_attendance
            member_object["church_attendance"] = attendance.church_attendance
        else:
            member_object["bussell_attendance"] = False
            member_object["church_attendance"] = False
        
        response_list.append(member_object)
    
    return JsonResponse(response_list, safe=False, status=200)

# this updates the church attendance of a particular bussell report for a particular bussell
@csrf_exempt
def update_church_attendance(request):
    bussell_report_id    = request.POST["report_id"]
    church_absence_list  = eval(request.POST["absence_list"])
    church_presence_list = eval(request.POST["presence_list"])
    
    print church_absence_list
    print church_presence_list
    
    bussell_report = BusselReport.objects.get(pk=bussell_report_id)
    
    for member_id in church_presence_list:
        
        member = BussellMember.objects.get(pk=member_id)
        try:
            attendance = BussellMemberAttendance.objects.get(
                bussell_report=bussell_report,
                bussell_member=member)
            attendance.church_attendance = True
            attendance.save()
            
        except BussellMemberAttendance.DoesNotExist:
            attendance = BussellMemberAttendance.objects.create(
                bussell_member = member,
                bussell_report = bussell_report,
                bussell_attendance = False,
                church_attendance = True)
            attendance.save()
            
    for member_id in church_absence_list:
        member = BussellMember.objects.get(pk=member_id)
        try:
            attendance = BussellMemberAttendance.objects.get(
                bussell_report=bussell_report,
                bussell_member=member)
            if attendance.bussell_attendance == False:
                attendance.delete()
                
            else:
                attendance.church_attendance = False
                attendance.save()
                
        except BussellMemberAttendance.DoesNotExist:
            pass
    
    attendances = BussellMemberAttendance.objects.filter(bussell_report=bussell_report, church_attendance=True)
    print attendances
    bussell_report.church_attendance = attendances.count()
    bussell_report.save()
    return HttpResponse(status=200)
                
# this saves a bussell member
@csrf_exempt
def save_bussell_member(request):
    first_name = request.POST["first_name"]
    other_names = request.POST["other_names"]
    phone = request.POST["phone"]
    date_of_birth = request.POST["date_of_birth"]
    date_joined = request.POST["date_joined"]
    address = request.POST["address"]
    gender = request.POST["gender"]
    church_member = request.POST["church_member"]

    profile = request.POST["profile"]
    bussell = request.POST["bussell_id"]
    
    print address

    bussell_member = BussellMember()
    bussell_member.first_name = first_name
    bussell_member.other_names = other_names
    bussell_member.phone = phone
    bussell_member.date_of_birth = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y").date()
    bussell_member.date_joined = datetime.datetime.strptime(date_joined, "%d/%m/%Y").date()
    bussell_member.address = address
    bussell_member.gender = int(gender)
    bussell_member.church_member = church_member=="True"
    bussell_member.bussell = Bussel.objects.get(pk=int(bussell))
    bussell_member.profile_pic = profile
    bussell_member.save()
    
    if bussell_member.pk is not None:
        return JsonResponse({"member_id": bussell_member.pk} , safe=False, status=200)
    return HttpResponse(status=401)

def get_all_bussell_members(request):
    bussell_id = request.GET["bussell_id"]
    bussell = Bussel.objects.get(pk=bussell_id)
    
    try:
        members = BussellMember.objects.filter(bussell=bussell)
        members_list = []
        for member in members:
            member_dict = {}
            member_dict["id"]      = member.pk
            member_dict["name"]    = member.first_name +" "+ member.other_names
            member_dict["phone"]   = member.phone
            member_dict["address"] = member.address
            member_dict["image"]   = member.profile_pic
            member_dict["church_member"] = member.church_member
            member_dict["gender"] = member.gender
            members_list.append(member_dict)
    
    except BussellMember.DoesNotExist:
        return JsonResponse(status=404)
    
    return JsonResponse(members_list, safe=False, status=200)

def export_bussels_list(request):
    export_type = request.GET["export_type"]

    # export as MS-EXCEL
    if export_type == "excel":
        import xlwt

    # export as PDF
    elif export_type == "pdf":
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter, inch, A4, landscape
        from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER

        bussels_all = Bussel.objects.all()

        # check if the list is empty
        if not bussels_all:
            pass
            #TODO 
            # tell the client that this list is empty using a message

        # list is not empty
        else:
            data = []
            header = ["R/N", "Bussell Name", "Bussell Code", "Bussell Leader", "Bussell Location", 
                      "Date Created"]
            data.append(header)
            bussel_each = []
            for index, bussel in enumerate(bussels_all):
                bussel_each.append(index + 1)
                bussel_each.append(bussel.name)
                bussel_each.append(bussel.code)
                bussel_each.append(bussel.leader)
                bussel_each.append("HNo. " + bussel.house_number +", " + bussel.street_name + 
                                   ", " + bussel.suburb)
                bussel_each.append(bussel.date_created)

                # add this bussel information to our data table
                data.append(bussel_each)
                bussel_each = []

            print data

            # make the pdf document
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="bussels_list.pdf"'
            doc = SimpleDocTemplate(response, pagesize=A4,
                                    rightMargin=72, topMargin=30)
            doc.pagesize = landscape(A4)

            # container to hold flowables
            elements = []

            table_style = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.0, colors.black),
                                   ('INNERGRID', (0,0), (-1, 0), 1.5, colors.black),
                                   ('TEXTFONT', (0,0), (-1, 0), 'Times-Bold'),
                                   ('BOX', (0,0), (-1,0), 1.5, colors.black),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                                   ('BOX', (0,1), (-1,-1), 1.5, colors.black)])

            title_style = ParagraphStyle(
                           name = 'title',
                           spaceAfter=20,
                           fontSize=24,
                           alignment=TA_CENTER
            )

            subtitle_style = ParagraphStyle(
                              name = 'subtitle',
                              spaceAfter=20,
                              fontSize = 14,
                              alignment=TA_CENTER
            )

            branch_style = ParagraphStyle(
                              name = 'branch', 
                              spaceAfter=20,
                              fontSize = 18,
                              alignment=TA_CENTER
            )

            title = 'Lighthouse Chapel International'
            branch = 'Darkuman Branch'
            subtitle = 'All Registered Bussells (Generated ' + datetime.datetime.now().strftime("%c") + ')'

            elements.append(Paragraph(title, title_style))
            elements.append(Paragraph(branch, branch_style))
            elements.append(Paragraph(subtitle, subtitle_style))

            table = Table(data)
            table.setStyle(table_style)

            for each in range(1, len(data)):
                if each % 2 == 0:
                    bg_color = colors.whitesmoke
                else:
                    bg_color = colors.white

                table.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

            elements.append(table)
            doc.build(elements)

            return response


def export_bussel_reports(request):
    export_type = request.GET["export_type"]

    # export as MS-EXCEL
    if export_type == "excel":
        import xlwt

    # export as PDF
    elif export_type == "pdf":
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter, inch, A4, landscape
        from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, TableStyle
        from reportlab.platypus.flowables import Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER

        request_date = request_date_wrapper.get_request_date()

        bussel_reports = BusselReport.objects.filter(date=request_date)

        if not bussel_reports:
            pass

        else:
            offertory_total = bussel_reports.aggregate(Sum('offertory_given'))
            souls_won_total = bussel_reports.aggregate(Sum('num_souls_won'))
            bussel_attendance_total = bussel_reports.aggregate(Sum('bussel_attendance'))
            church_attendance_total = bussel_reports.aggregate(Sum('church_attendance'))
            first_timers_total = bussel_reports.aggregate(Sum('num_first_timers'))
            data = []
            header = ["R/N", "Bussell Name","Bussell Code", "Bussell Leader", "Topic Taught", 
                      "B/A", "C/A", "Of(GHC)", "F/T", "S/W"]
            data.append(header)
            bussel_each = []
            for index, report in enumerate(bussel_reports):
                bussel_each.append(index + 1)
                bussel_each.append(report.bussel.name)
                bussel_each.append(report.bussel.code)
                bussel_each.append(report.bussel.leader)
                bussel_each.append(report.topic)
                bussel_each.append(report.bussel_attendance)
                bussel_each.append(report.church_attendance)
                bussel_each.append("{0:.2f}".format(report.offertory_given))
                bussel_each.append(report.num_first_timers)
                bussel_each.append(report.num_souls_won)

                # add this bussel information to our data table
                data.append(bussel_each)
                bussel_each = []


            data.append(["", "", "", "", "", bussel_attendance_total["bussel_attendance__sum"],
                         church_attendance_total["church_attendance__sum"], 
                         "{0:.2f}".format(offertory_total["offertory_given__sum"]), 
                         first_timers_total["num_first_timers__sum"],
                         souls_won_total["num_souls_won__sum"]])
            # make the pdf document
            response = HttpResponse(content_type='application/pdf')
            file_name = "bussel_reports(" +  \
                         request_date_wrapper.get_request_date().strftime('%d/%b/%Y') + ").pdf"
            response['Content-Disposition'] = 'inline; filename=' + file_name
            doc = SimpleDocTemplate(response, pagesize=A4,
                                    rightMargin=24, topMargin=30)
            doc.pagesize = landscape(A4)

            # container to hold flowables
            elements = []

            table_style = TableStyle([('INNERGRID', (0,0), (-1,-2), 0.0, colors.black),
                                   ('INNERGRID', (0,0), (-1, 0), 1.5, colors.black),
                                   ('INNERGRID', (5,-1), (-1, -1), 1.5, colors.black),
                                   ('TEXTFONT', (0,0), (-1, 0), 'Times-Bold'),
                                   ('BOX', (0,0), (-1,0), 1.5, colors.black),
                                   ('BOX', (5,-1), (-1,-1), 1.5, colors.black),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                                   ('BACKGROUND', (5, -1), (-1, -1), colors.lightgrey),
                                   ('ALIGN', (5, 1), (-1, -1), 'RIGHT'),
                                   ('BOX', (0,1), (-1,-2), 1.5, colors.black)])

            title_style = ParagraphStyle(
                           name = 'title',
                           spaceAfter=20,
                           fontSize=24,
                           alignment=TA_CENTER
            )

            subtitle_style = ParagraphStyle(
                              name = 'subtitle',
                              spaceAfter=20,
                              fontSize = 14,
                              alignment=TA_CENTER
            )

            branch_style = ParagraphStyle(
                              name = 'branch', 
                              spaceAfter=20,
                              fontSize = 18,
                              alignment=TA_CENTER
            )

            title = 'Lighthouse Chapel International'
            branch = 'Darkuman Branch'
            subtitle = 'Bussell Reports for ' + request_date_wrapper.get_request_date().strftime('%d/%b/%Y')

            elements.append(Paragraph(title, title_style))
            elements.append(Paragraph(branch, branch_style))
            elements.append(Paragraph(subtitle, subtitle_style))


            table = Table(data)
            table.setStyle(table_style)

            for each in range(1, len(data)-1):
                if each % 2 == 0:
                    bg_color = colors.whitesmoke
                else:
                    bg_color = colors.white

                table.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))
                table.setStyle(TableStyle([('INNERGRID', (0, each), (-1, each), 1.5, colors.black)]))

            elements.append(table)
            cols_sign = [["_______________________","_______________________", "______________________"  ],
                         ["Bussell Clerk", "Treasurer", "Pastor"]]
            table_sign = Table(cols_sign, colWidths=[180, 180, 180])
            elements.append(Spacer(1, 0.2*inch))
            elements.append(table_sign)
            doc.build(elements)

            return response

def get_reports_for_bussel(request):
    bussel_code     = request.GET["code"]
    bussel_password = request.GET["password"]

    if authenticate_bussel(bussel_code, bussel_password):
        try:
            reports_for_bussel = BusselReport.objects.filter(bussel=Bussel.objects.get(code=bussel_code)) \
                .order_by('-date')
            object_list = []
            for report in reports_for_bussel:
                object_dict = {}
                object_dict['pk'] = report.pk
                object_dict['b_attendance'] = report.bussel_attendance
                object_dict['c_attendance'] = report.church_attendance
                object_dict['start_time'] = report.time_started.strftime('%H:%M:%S')
                object_dict['end_time'] = report.time_ended.strftime('%H:%M:%S')
                object_dict['topic'] = report.topic
                object_dict['first_timers'] = report.num_first_timers
                object_dict['new_converts'] = report.num_souls_won
                object_dict['offering'] = report.offertory_given
                object_dict['date'] = report.date.strftime('%d-%b-%Y')
                object_dict['comments'] = report.notes
                object_dict['report_time'] = report.time
                object_list.append(object_dict)

        except BusselReport.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse(object_list, safe=False)

    else:
        return HttpResponse(status=401)

def get_dates_in_month(year, month, day_of_week):
    from calendar import weekday, monthrange

    days = [weekday(year, month, d+1) for d in range(monthrange(year, month)[1])]
    saturdays = [i+1 for i, x in enumerate(days) if x==day_of_week]
    return [datetime.date(year, month, d) for d in saturdays]

def export_bussel_monthly_reports(request):
    export_type = request.GET["export_type"]
    #month = request.GET["month"]

    # export as MS-EXCEL
    if export_type == "excel":
        import xlwt

    # export as PDF
    elif export_type == "pdf":
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter, inch, A4, landscape
        from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, TableStyle
        from reportlab.platypus.flowables import Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER


        bussells = Bussel.objects.filter(status=1)
        if not bussells:
            pass

        else:
            data = []
            header = ["R/N", "Bussell Name", "Bussell Leader"]
            bussell_dates = get_dates_in_month(2017, 9, 5)
            for d in bussell_dates:
                header.append(d.strftime('%d-%m-%Y'))
            data.append(header)
            bussel_each = []
            for index, bussell in enumerate(bussells):
                bussel_each.append(index + 1)
                bussel_each.append(bussell.name)
                bussel_each.append(bussell.leader)
                for date in bussell_dates:
                    for report in bussell.busselreport_set.filter(date__month=9):
                        if date == report.date:
                            bussel_each.append("B: " + str(report.bussel_attendance)+ ", " + "C: "+ str(report.church_attendance))                           

                # add this bussel information to our data table
                data.append(bussel_each)
                bussel_each = []


            # make the pdf document
            response = HttpResponse(content_type='application/pdf')
            file_name = "bussel_months_reports(" +  \
                         request_date_wrapper.get_request_date().strftime('%d/%b/%Y') + ").pdf"
            response['Content-Disposition'] = 'inline; filename=' + file_name
            doc = SimpleDocTemplate(response, pagesize=A4,
                                    rightMargin=24, topMargin=30)
            doc.pagesize = landscape(A4)

            # container to hold flowables
            elements = []

            table_style = TableStyle([('INNERGRID', (0,0), (-1,-2), 0.0, colors.black),
                                   ('INNERGRID', (0,0), (-1, -1), 1.5, colors.black),
                                   ('TEXTFONT', (0,0), (-1, 0), 'Times-Bold'),
                                   ('BOX', (0,0), (-1,-1), 1.5, colors.black),
                                   ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
                                   ('BOX', (0,1), (-1,-2), 1.5, colors.black)])

            title_style = ParagraphStyle(
                           name = 'title',
                           spaceAfter=20,
                           fontSize=24,
                           alignment=TA_CENTER
            )

            subtitle_style = ParagraphStyle(
                              name = 'subtitle',
                              spaceAfter=20,
                              fontSize = 14,
                              alignment=TA_CENTER
            )

            branch_style = ParagraphStyle(
                              name = 'branch', 
                              spaceAfter=20,
                              fontSize = 18,
                              alignment=TA_CENTER
            )

            title = 'Lighthouse Chapel International'
            branch = 'Darkuman Branch'
            subtitle = 'Bussell Reports Summary for September, 2017'  

            elements.append(Paragraph(title, title_style))
            elements.append(Paragraph(branch, branch_style))
            elements.append(Paragraph(subtitle, subtitle_style))


            table = Table(data)
            table.setStyle(table_style)

            for each in range(1, len(data)):
                if each % 2 == 0:
                    bg_color = colors.whitesmoke
                else:
                    bg_color = colors.white

                table.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))
                table.setStyle(TableStyle([('INNERGRID', (0, each), (-1, each), 1.5, colors.black)]))

            elements.append(table)
            doc.build(elements)

            return response

class BussellPerformanceMetricsView(TemplateView):
    template_name = "bussels_app/bussell_performance_metrics.html"
    login_url ="/login/"
    group_required= [u"Bussell", u"Manager"]
    raise_exception = show_access_denied_page

    def get_context_data(self, **kwargs):
        context = super(BussellPerformanceMetricsView, self).get_context_data(**kwargs)
        form = BussellPerformanceMetricsForm()
        context['form'] = form
        return context

def get_performance_data(request):
    pid = request.GET['pk']
    from_date = request.GET['from']
    to_date = request.GET['to']

    reports = BusselReport.objects.filter(bussel=pid, date__range=[from_date, to_date]).order_by('date')

    object_list = []

    date_labels = []
    bussell_attendance_list = []
    church_attendance_list = []

    for report in reports:
        bussell_attendance_list.append(report.bussel_attendance)
        church_attendance_list.append(report.church_attendance)
        date_labels.append(report.date)




    return JsonResponse([date_labels, bussell_attendance_list, church_attendance_list], safe=False)

def get_monthly_average(request):
    pid = request.GET['pk']

    print pid

    monthly_average = BusselReport.objects.filter(bussel=pid).annotate(month=Month('date'))\
                             .values('month')\
                             .annotate(avg_bu=Avg('bussel_attendance'))\
                             .annotate(avg_ch=Avg('church_attendance'))\
                             .order_by("month")

    response_list = []

    for ma in monthly_average:
        temp_list = []
        temp_list.append(calendar.month_name[ma.get('month')])
        temp_list.append(round(ma.get('avg_bu'),2))
        temp_list.append(round(ma.get('avg_ch'), 2))
        temp_list.append(round(ma.get('avg_ch')*100.0/ma.get('avg_bu'), 2))

        response_list.append(temp_list)
    
    return JsonResponse(response_list, safe=False)
