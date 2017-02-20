from django.contrib import admin
from info_system.models import Member, Ministry, Language

class MemberAdmin(admin.ModelAdmin):
    exclude = ('member_location',)
# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Ministry)
admin.site.register(Language)

