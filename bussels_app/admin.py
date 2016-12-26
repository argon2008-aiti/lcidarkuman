from django.contrib import admin
from bussels_app.models import Bussel

class BusselAdmin(admin.ModelAdmin):
    exclude = ('bussel_location', 'code')
admin.site.register(Bussel, BusselAdmin)
