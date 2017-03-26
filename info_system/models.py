from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField
import datetime

MARITAL_STATUS = [
(0, "Single"),
(1, "Married"),
(2, "Separated"),
(3, "Divorced"),
(4, "Widowed")
]

EDUCATION_LEVEL = [
(0, "None"),
(1, "Primary"),
(2, "Junior High School"),
(3, "Senior High School"),
(4, "First Degree"),
(5, "Second Degree"),
(6, "Doctorate Degree")
]

GENDER = [
(0, "Male"),
(1, "Female")
]

LANGUAGES = [
(0, "English"),
(1, "French"),
(2, "Akan"),
(3, "Ga"),
(4, "Ewe"),
(5, "Hausa"),
]

YES_NO = [
(0, "No"),
(1, "Yes")
]

MEMBERSHIP_STATUS= [
(0, "Inactive"),
(1, "Active")
]

ROLES = [
(0, "None"),
(1, "Pastor"),
(2, "Lady Pastor"),
(3, "Bussell Leader"),
(4, "Ministry Leader")
]

NATIONALITY = [
(0, "Ghanaian"),
(1, "Nigerian"),
(2, "Togolese"),
(3, "Beninois")
]

class Ministry(models.Model):
    name = models.CharField(max_length=50)
    purpose = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name 

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Member(models.Model):
    # personal info ----------------------------
    first_name     = models.CharField(max_length=20)
    middle_name    = models.CharField(max_length=20)
    last_name      = models.CharField(max_length=20)
    gender         = models.IntegerField(choices=GENDER, default=0)
    phone          = models.CharField(max_length=15)
    marital_status = models.IntegerField(choices=MARITAL_STATUS, default=0)
    profile        = models.ImageField(upload_to="static/profiles/", blank=True, \
                                       default="static/profiles/default.png")
    date_of_birth  = models.DateField(default=datetime.date.today())
    place_of_birth = models.CharField(max_length=100, default="Accra")
    nationality    = models.IntegerField(choices=NATIONALITY)
    nationality_at_birth = models.IntegerField(choices=NATIONALITY)
    hometown       = models.CharField(max_length=200, default="Madina, Greater Accra, Ghana")
    tribal_origin  = models.CharField(max_length=200, default="Asante, Asante Region, Ghana")
    email_address  = models.EmailField(null=True, blank=True)
    lingual_competency = models.ManyToManyField(Language)
    level_of_education = models.IntegerField(choices=EDUCATION_LEVEL, default=0)
    occupation = models.CharField(max_length=100, default="Unemployed")

    # address ----------------------------------
    house_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=50, blank=True, null=True)
    suburb      = models.CharField(max_length=50, blank=True, null=True)
    description_of_house = models.CharField(max_length=300, blank=True, null=True)
    member_location = PointField(null=True)

    # church info ------------------------------
    date_joined = models.DateField(default=datetime.date.today())
    baptized_by_immersion = models.IntegerField(choices=YES_NO, default=1)
    holy_ghost_baptism    = models.IntegerField(choices=YES_NO, default=0)
    leadership_role = models.IntegerField(choices=ROLES, default=0)
    ministries = models.ManyToManyField(Ministry, blank=True, null=True)
    membership_status = models.IntegerField(choices=MEMBERSHIP_STATUS, default=1)

    def __unicode__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

class Manager(models.Model):
    user = models.OneToOneField(User)

class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=250)
    member = models.ForeignKey(Member)

    def __unicode__(self):
        return self.date + " -- " + self.member.first_name + " " + self.member.last_name



