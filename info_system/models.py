from django.db import models
from djgeojson.fields import PointField

MARITAL_STATUS = [
(0, "single"),
(1, "married"),
(2, "divorced")
]

GENDER = [
(0, "Male"),
(1, "Female")
]

class Member(models.Model):
    # personal info ----------------------------
    first_name     = models.CharField(max_length=20)
    middle_name    = models.CharField(max_length=20)
    last_name      = models.CharField(max_length=20)
    gender         = models.IntegerField(choices=GENDER, default=0)
    phone          = models.CharField(max_length=15)
    marital_status = models.IntegerField(choices=MARITAL_STATUS, default=0)
    profile        = models.ImageField(upload_to="static/profiles/", blank=True, null=True)

    # address ----------------------------------
    house_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    suburb      = models.CharField(max_length=50)
    member_location    = PointField(null=True)

    def __unicode__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name
