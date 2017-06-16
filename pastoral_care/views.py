from django.shortcuts import render
from info_system.views import *
from django.http import JsonResponse, HttpResponse
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from info_system.models import Member
from forms import NewMemberForm
import datetime

class MemberShipListView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "pastoral_care/all_members.html"
    login_url     = "/login/"
    group_required = [u"Pastoral Care", u"Manager"]
    raise_exception = show_access_denied_page

class MemberDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    template_name = "pastoral_care/member_detail.html"
    model = Member
    login_url = "/login/"
    group_required = [u"Pastoral Care", u"Manager"]
    raise_exception = show_access_denied_page

    def get_context_data(self, **kwargs):
        context = super(MemberDetailView, self).get_context_data(**kwargs)
        print self.object
        languages = [language.name for language in self.object.lingual_competency.all()]
        print languages
        context['languages'] = languages 
        return context

class MemberEditView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    template_name = "pastoral_care/add_new_member.html"
    login_url = "/login/"
    group_required = [u"Pastoral Care", u"Manager"]
    raise_exception = show_access_denied_page

    def get_context_data(self, **kwargs):
        from django.forms.models import model_to_dict
        self.object = None
        context = super(MemberEditView, self).get_context_data(**kwargs)

        member = Member.objects.get(pk=kwargs['pk'])
        member_form = NewMemberForm(initial=model_to_dict(member))
        context["title"] = "Edit Member"
        context["subtitle"] = "Edit this Member"
        context["form"] = member_form
        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        form = NewMemberForm(request.POST)
        print form

        if form.is_valid():
            member = Member.objects.get(pk=kwargs['pk'])
            member.first_name = form.cleaned_data['first_name'] 
            member.middle_name = form.cleaned_data['middle_name'] 
            member.last_name = form.cleaned_data['last_name'] 
            member.phone = form.cleaned_data['phone'] 
            member.email_address = form.cleaned_data['email_address'] 
            member.gender = form.cleaned_data['gender'] 
            member.marital_status = form.cleaned_data['marital_status'] 
            member.date_of_birth = form.cleaned_data['date_of_birth'] 
            member.place_of_birth = form.cleaned_data['place_of_birth'] 
            member.occupation = form.cleaned_data['occupation']
            member.lingual_competency = form.cleaned_data['lingual_competency']
            member.level_of_education = form.cleaned_data['level_of_education']
            member.nationality_at_birth = form.cleaned_data['nationality_at_birth'] 
            member.nationality = form.cleaned_data['nationality'] 

            member.house_number = form.cleaned_data['house_number'] 
            member.street_name = form.cleaned_data['street_name'] 
            member.suburb = form.cleaned_data['suburb'] 
            member.description_of_house = form.cleaned_data['description_of_house'] 

            member.date_joined = form.cleaned_data['date_joined'] 
            member.baptized_by_immersion = form.cleaned_data['baptized_by_immersion'] 
            member.holy_ghost_baptism = form.cleaned_data['holy_ghost_baptism'] 
            member.leadership_role = form.cleaned_data['leadership_role'] 
            member.membership_status = form.cleaned_data['membership_status'] 
            member.ministries = form.cleaned_data['ministries']

            member.save()
            return redirect(reverse("pastoral:all-members"))
        
        return render(request, self.template_name, self.get_context_data(**kwargs))

class AddNewMemberView(LoginRequiredMixin, GroupRequiredMixin, FormView):
    template_name = "pastoral_care/add_new_member.html"
    login_url     = "/login/"
    group_required = [u"Pastoral Care", u"Manager"]
    raise_exception = show_access_denied_page
    success_url = "/pastoral/members/all" 

    def get_context_data(self, **kwargs):
        context = super(AddNewMemberView, self).get_context_data(**kwargs)
        context["title"] = "New Member"
        context["subtitle"] = "Add New Member"
        return context

    def form_valid(self, form):
        new_member = Member.objects.create(
                     first_name = form.cleaned_data['first_name'], 
                     middle_name = form.cleaned_data['middle_name'], 
                     last_name = form.cleaned_data['last_name'], 
                     phone = form.cleaned_data['phone'], 
                     email_address = form.cleaned_data['email_address'], 
                     gender = form.cleaned_data['gender'], 
                     marital_status = form.cleaned_data['marital_status'], 
                     date_of_birth = form.cleaned_data['date_of_birth'], 
                     place_of_birth = form.cleaned_data['place_of_birth'], 
                     occupation = form.cleaned_data['occupation'],
                     level_of_education = form.cleaned_data['level_of_education'],
                     nationality_at_birth = form.cleaned_data['nationality_at_birth'], 
                     nationality = form.cleaned_data['nationality'], 

                     house_number = form.cleaned_data['house_number'], 
                     street_name = form.cleaned_data['street_name'], 
                     suburb = form.cleaned_data['suburb'], 
                     description_of_house = form.cleaned_data['description_of_house'], 

                     date_joined = form.cleaned_data['date_joined'], 
                     baptized_by_immersion = form.cleaned_data['baptized_by_immersion'], 
                     holy_ghost_baptism = form.cleaned_data['holy_ghost_baptism'], 
                     leadership_role = form.cleaned_data['leadership_role'], 
                     membership_status = form.cleaned_data['membership_status'],
        )
        new_member.ministries = form.cleaned_data['ministries']
        new_member.lingual_competency = form.cleaned_data['lingual_competency']
        new_member.save()

        return super(AddNewMemberView, self).form_valid(form)

    def form_invalid(self, form):
        print form
        return super(AddNewMemberView, self).form_invalid(form)
    

def json_member_list(request):
    
    if request.method == "GET":
        members = Member.objects.all()
        object_list = []

        for member in members:
            object_dict = {}
            object_dict['pk'] = member.pk
            object_dict['first_name'] = member.first_name
            object_dict['middle_name'] = member.middle_name
            object_dict['surname'] = member.last_name
            object_dict['phone'] = member.phone
            object_dict['street_name'] = member.street_name
            object_dict['suburb'] = member.suburb
            object_dict['profile_url'] = member.profile.url

            object_list.append(object_dict)

        return JsonResponse(object_list, safe=False)
def add_footer_note(canvas, doc):
    from reportlab.lib.units import mm
    timestamp = datetime.datetime.now().strftime("%c")
    canvas.drawRightString(200*mm, 15*mm, "accessed: "+timestamp)

def export_members(request):

    export_type = request.GET['export_type']

    #export as MS-EXCEL
    if export_type == "excel":
        import xlwt

    #export as PDF
    elif export_type == "pdf":
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter, inch, A4, landscape
        from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
        from reportlab.pdfgen import canvas
        
        all_members = Member.objects.all()

        if not all_members:
            pass
            #TODO
            # request returned no data

        else:
            data = []
            header = ["R/N", "Name","Gender", "Mobile Number","Marital Status", "Location", "Status"]
            data.append(header)
            member_each = []

            for index, member in enumerate(all_members):
                member_each.append(index + 1)
                member_each.append(member.first_name + " " + member.middle_name + " " + member.last_name)
                member_each.append(member.get_gender_display())
                member_each.append(member.phone)
                member_each.append(member.get_marital_status_display())
                member_each.append(member.suburb)
                member_each.append(member.get_membership_status_display())

                data.append(member_each)
                member_each = []
            print data

            #make the pdf document
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="all members.pdf"'

            doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, topMargin=30)

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
            subtitle = 'All Registered Church Members' 
            
            elements.append(Paragraph(title, title_style))
            elements.append(Paragraph(branch, branch_style))
            elements.append(Paragraph(subtitle, subtitle_style))

            table = Table(data)
            table.setStyle(table_style)

            # alternating row colors
            for each in range(1, len(data)):
                if each % 2 == 0:
                    bg_color = colors.whitesmoke
                else:
                    bg_color = colors.white

                table.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

            elements.append(table)
            doc.build(elements, 
                      onFirstPage=add_footer_note,
                      onLaterPages=add_footer_note)

            return response

def is_member_pastoral(user):
    return user.groups.filter(name="Pastoral").exists() or user.is_superuser

@csrf_exempt
def authorize_attendance(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)

    if user is not None and is_member_pastoral(user):
        return HttpResponse("AUTHORIZED", status=200)
    else:
        return HttpResponse("UNAUTHORIZED", status=401)

