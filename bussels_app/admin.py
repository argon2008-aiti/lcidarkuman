from django.contrib import admin
from bussels_app.models import Bussel, BusselReport, BussellMember, BussellMemberAttendance

class BusselAdmin(admin.ModelAdmin):
    exclude = ('bussel_location', 'code')

class BusselReportAdmin(admin.ModelAdmin):
    pass

class BussellMemberAdmin(admin.ModelAdmin):
    pass

class BussellMemberAttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bussel, BusselAdmin)
admin.site.register(BusselReport, BusselReportAdmin)
admin.site.register(BussellMember, BussellMemberAdmin)
admin.site.register(BussellMemberAttendance, BussellMemberAttendanceAdmin)
