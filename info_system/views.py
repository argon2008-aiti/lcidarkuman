from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.view.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def show_access_denied_page(caller, request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    return redirect(reverse('access-denied'))

@csrf_exempt
def log_in_shepherd(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username, password)
    if user is not None:
        return HttpResponse("OK")
    else:
        return HttpResponse("UNAUTHORIZED")
