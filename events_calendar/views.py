from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from models import EventCalendar, RecurringEventCalendar
from django.views.decorators.csrf import csrf_exempt
import datetime


def event_calendar_list_json(request):
    events = EventCalendar.objects.all()
    event_list = []
    for event in events:
        event_dict = {}
        event_dict['title'] = event.title
        event_dict['description'] = event.description
        event_dict['location'] = event.location
        event_dict['start'] = event.start_date_time.strftime("%s")
        event_dict['end'] = event.end_date_time.strftime("%s")
        event_list.append(event_dict)

    for event in RecurringEventCalendar.objects.all():
        for date in weekday_occurences(event.start_date_time, 
                                       event.end_date_time, event.day):
            event_dict = {}
            event_dict['title'] = event.title
            event_dict['description'] = event.description
            event_dict['location'] = event.location
            event_dict['start'] = date.strftime("%s")
            event_dict['end'] = date.strftime("%s")

            event_list.append(event_dict)

    return JsonResponse(event_list, safe=False, status=200)

@csrf_exempt
def add_event_calendar(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    start = request.POST.get('start')
    end = request.POST.get('end')

    n = datetime.datetime.now()

    if int(start)<int(n.strftime("%s")) or \
            int(end)<int(n.strftime("%s")):
        return HttpResponse(status=400)

    else:
        event = EventCalendar(
            title = title,
            description = description,
            location = location,
            start_date_time = datetime.datetime.utcfromtimestamp(int(start)),
            end_date_time = datetime.datetime.utcfromtimestamp(int(end)))

        event.save()
        return HttpResponse(status=200)

@csrf_exempt
def add_recurring_event(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    start = request.POST.get('start')
    end = request.POST.get('end')
    day = request.POST.get('day')

    event = RecurringEventCalendar(
            title = title,
            description = description,
            location = location,
            start_date_time = datetime.datetime.utcfromtimestamp(int(start)),
            end_date_time = datetime.datetime.utcfromtimestamp(int(end)),
            day =day)

    event.save()
    return HttpResponse(status=200)


def weekday_occurences(start_date, end_date, weekday):
    date_list = []

    next_occurence = start_date + datetime.timedelta(weekday-start_date.weekday())
    while(next_occurence<=end_date):
        date_list.append(next_occurence)
        next_occurence = next_occurence + datetime.timedelta(7)
    
    return date_list

