from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def show_access_denied_page(caller, request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    return redirect(reverse('access-denied'))
