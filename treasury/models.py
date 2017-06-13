from django.db import models
from info_system.models import Member

MONTHS = [
    (0, "January"),
    (1, "February"),
    (2, "March"),
    (3, "April"),
    (4, "May"),
    (5, "June"),
    (6, "July"),
    (7, "August"),
    (8, "September"),
    (9, "October"),
    (10, "November"),
    (11, "December"),
]

class Offering(models.Model):
    description = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __unicode__(self):
        return self.description + " " + self.date.strftime("%d-%m-%Y") +  " -- " + str(self.amount)

class Tithe(models.Model):
    member = models.ForeignKey(Member)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.member.first_name + " " + self.member.last_name + " " + \
            ", "+ self.get_month_display() + " -- " + str(self.amount)
