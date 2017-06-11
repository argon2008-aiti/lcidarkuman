from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from models import Offering, Tithe
from info_system.models import Member
import datetime


def is_treasurer(user):
    return user.groups.filter(name="Finance").exists()

@csrf_exempt
def get_all_offerings(request):

    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(username=username, password=password)

    if user is not None and is_treasurer(user):
        offerings = Offering.objects.all()

        offering_list = []
        for offering in offerings:
            object_dict = {}

            object_dict["description"] = offering.description
            object_dict["date"] = offering.date
            object_dict["amount"] = offering.amount

            offering_list.append(object_dict)
        return JsonResponse(offering_list, safe=False)

    else:
        return HttpResponse("UNAUTHORIZED", status=401)

@csrf_exempt
def add_offering(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(username=username, password=password)

    if user is not None and is_treasurer(user):

        date = datetime.datetime.strptime(request.POST["date"], "%d-%m-%Y").date()

        offering = Offering(description=request.POST["description"], \
                            amount=request.POST["amount"], \
                            date=date \
                            )
        offering.save()

        return HttpResponse("OK", status=200)

    else:
        return HttpResponse("UNAUTHORIZED", status=401)
        

@csrf_exempt
def get_all_tithes(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(username=username, password=password)

    if user is not None and is_treasurer(user):
        tithes = Tithe.objects.all()

        tithe_list = []
        for tithe in tithes:
            object_dict = {}

            object_dict["member"] = tithe.member.first_name + " " \
                          + tithe.member.middle_name + " " + tithe.member.last_name
            object_dict["month"] = tithe.month
            object_dict["year"] = tithe.year
            object_dict["amount"] = tithe.amount
            object_dict["pk"] = tithe.member.pk

            tithe_list.append(object_dict)
        return JsonResponse(tithe_list, safe=False)

    else:
        return HttpResponse("UNAUTHORIZED", status=401)

@csrf_exempt
def add_tithe(request):

    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(username=username, password=password)

    if user is not None and is_treasurer(user):

        member = Member.objects.get(pk=request.POST["pk"])

        tithe = Tithe(member=member, \
                            amount=request.POST["amount"], \
                            month=request.POST["month"], \
                            year=request.POST["year"] \
                            )
        tithe.save()

        return HttpResponse("OK", status=200)

    else:
        return HttpResponse("UNAUTHORIZED", status=401)
