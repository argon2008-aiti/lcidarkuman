from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


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
        json_object["last_name"] = shepherd.member.last_name

        return JsonResponse(json_object, safe=False)
    else:
        return HttpResponse("UNAUTHORIZED", status=401)

def change_password(request):
    pass
