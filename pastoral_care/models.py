from django.db import models

from info_system.models import Member

class MasterAttendance(models.Model):
    description = models.CharField(max_length=2048)
    authorized_by = models.ForeignKey(Member)
    date_time = models.DateTimeField(auto_now=True)

class MemberAttendance(models.Model):
    master_attendance = models.ForeignKey(MasterAttendance)
    member = models.ForeignKey(Member)


