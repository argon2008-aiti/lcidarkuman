from django.db import models
from django.contrib.postgres.fields import ArrayField
from info_system.models import Member
from django.core.exceptions import ValidationError

class MasterAttendance(models.Model):
    description = models.CharField(max_length=2048)
    authorized_by = models.ForeignKey(Member)
    in_session = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now=True)

class MemberAttendance(models.Model):
    master_attendance = models.ForeignKey(MasterAttendance)
    member = models.ForeignKey(Member)

class AttendanceOfficer(models.Model):
    shepherd_pk = models.IntegerField()
    assigned_members = ArrayField(models.IntegerField())

class AttendanceConfiguration(models.Model):
    attendance_in_session = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if AttendanceConfiguration.objects.exists() and not self.pk:
            raise ValidationError("Only one instance allowed here")
        else:
            return super(AttendanceConfiguration, self).save(*args, **kwargs)

def get_attendance_session_status():
    config = AttendanceConfiguration.objects.first()
    if config is None:
        config = AttendanceConfiguration()
        config.save()
    return config.attendance_in_session

def set_attendance_session_status(status):
    config = AttendanceConfiguration.objects.first()
    if config is None :
        config = AttendanceConfiguration()
    config.attendance_in_session = status
    config.save()

