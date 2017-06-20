from django.shortcuts import render
from braces.views import LoginRequiredMixin
from models import Notice
from django.views.decorators.csrf import csrf_exempt
from django.utils import dateformat
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse

import string

@csrf_exempt
def add_notice(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    # check if this is a shepherd
    if authenticate_user(username, password):
        # get notice from request
        title = request.POST["title"]
        content = request.POST["content"]

        # save notice in db
        notice = Notice.objects.create(title=title, content=content, \
                               creator=User.objects.get(username=username))
        notice.save()

        return HttpResponse(status=200)

    else:
        return HttpResponse(status=403)

    return HttpResponse(status=401)

def notice_list_json(request):
    if request.method=="GET":
        notices = Notice.objects.all()

        object_list = []

        for notice in notices:
            object_dict = {}

            object_dict['pk'] = notice.pk
            object_dict['title'] = string.capwords(notice.title)
            object_dict['date'] = dateformat.format(notice.date, 'U')
            object_dict['content'] = notice.content
            object_dict['creator'] = notice.creator.shepherd.member.first_name + \
                " " + notice.creator.shepherd.member.last_name

            object_list.append(object_dict)

        return JsonResponse(object_list, safe=False)
    else:
        return HttpResponse(status=403)
    
    return HttpResponse(status=401)

def authenticate_user(username, password):
    return authenticate(username=username, password=password)
