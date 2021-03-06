from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from models import Shepherd


def show_access_denied_page(caller, request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    return redirect(reverse('access-denied'))

@csrf_exempt
def log_in_shepherd(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username=username, password=password)
    if user is not None:
        shepherd = Shepherd.objects.get(user=user)
        json_object = {}
        json_object["first_name"] = shepherd.member.first_name
        json_object["middle_name"] = shepherd.member.middle_name
        json_object["last_name"] = shepherd.member.last_name
        json_object["profile"] = shepherd.member.profile.url

        return JsonResponse(json_object, safe=False)
    else:
        return HttpResponse("UNAUTHORIZED", status=401)

def change_password(request):
    pass


@csrf_exempt
def treasury_authenticate(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username=username, password=password)

    if user is not None and user.groups.filter(name="Finance").exists():
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)
