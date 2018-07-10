from django.db import models
from djgeojson.fields import PointField
from info_system.models import Member
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import *
from django.utils.crypto import get_random_string

from django.db.models import Func, F, Sum

DAYS = [
    (0, "Sunday"),
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
]

STATUS = [
    (0, "Inactive"),
    (1, "Active"),
]

GENDER = [
    (0, "Male"),
    (1, "Female"),
]

class Bussel(models.Model):
    # Bussel Information ---------------------
    name            = models.CharField(max_length=50)
    code            = models.CharField(max_length=10)
    zone            = models.CharField(max_length=5)
    meeting_day     = models.IntegerField(choices=DAYS)
    meeting_time    = models.TimeField()
    password        = models.CharField(max_length=100) 

    # Bussel Location ------------------------
    house_number    = models.CharField(max_length=50)
    street_name     = models.CharField(max_length=50)
    suburb          = models.CharField(max_length=50)
    bussel_location = PointField(null=True)

    # Bussel Leader --------------------------
    leader = models.ForeignKey(Member)

    # Meta Data ------------------------------
    status       = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateField(auto_now_add=True)

    group_pic = models.URLField(null=True, max_length=400)

    def __unicode__(self):
        return self.name + " (" + self.leader.first_name + " " + self.leader.last_name + ")"


# Weekly Report ------------------------------
class BusselReport(models.Model):
    bussel             = models.ForeignKey(Bussel)
    topic              = models.CharField(max_length=100)
    date               = models.DateField()
    time               = models.TimeField(auto_now_add=True)
    time_started       = models.TimeField()
    time_ended         = models.TimeField()
    bussel_attendance  = models.IntegerField()
    church_attendance  = models.IntegerField(default=0)
    num_souls_won      = models.IntegerField()
    num_first_timers   = models.IntegerField()
    offertory_given    = models.FloatField()

    class Meta:
        get_latest_by = 'date'

    def __unicode__(self):
        return self.bussel.name + "--" + self.topic

class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()

class BussellMember(models.Model):
    first_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True)
    date_of_birth = models.DateField()
    date_joined = models.DateField()
    gender = models.IntegerField(choices=GENDER, default=0)
    church_member = models.BooleanField(default=False)
    profile_pic = models.URLField(null=True, max_length=400)
    bussell = models.ForeignKey(Bussel)
    
    def __unicode__(self):
        return self.bussell.name + " -> " self.first_name+ " "+self.other_names

# Generate unique xxxx-xxxx hex code for each bussel
def get_hex_code():
    allowed_chars = 'ABCDEF0123456789'
    code = get_random_string(length=4, allowed_chars=allowed_chars) + \
        "-" + get_random_string(length=4, allowed_chars=allowed_chars)
    return code


# Signals --------------------------------------

# hash raw password from form
@receiver(pre_save, sender=Bussel)
def hash_password(sender, **kwargs):
    raw_password = kwargs['instance'].password
    if is_password_usable(raw_password):
        return
    else:
        hashed_password = make_password(raw_password)
        kwargs['instance'].password = hashed_password
    return


# get a unique hex code 
@receiver(pre_save, sender=Bussel)
def save_hex_code(sender, **kwargs):
    bussel = kwargs['instance']
    if bussel.pk is not None:
        print "already has code"
        return
    code = get_hex_code()
    existing_codes = Bussel.objects.all().values_list('code')
    while code in existing_codes:
        code = get_hex_code()
    bussel.code = code
    print code
    return

