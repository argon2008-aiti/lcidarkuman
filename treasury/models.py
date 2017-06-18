from django.db import models
from info_system.models import Member
import datetime

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


def get_week_number(p_date):
    return p_date.isocalendar()[1]


class Offering(models.Model):
    description = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    week_number = models.IntegerField()

    def __unicode__(self):
        return self.description + " " + self.date.strftime("%d-%m-%Y") +  " -- " + str(self.amount)

    def save(self, *args, **kwargs):
        self.week_number = get_week_number(self.date)
        return super(Offering, self).save(*args, **kwargs)

class Tithe(models.Model):
    member = models.ForeignKey(Member)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField()
    date = models.DateField(auto_now=True)
    week_number = models.IntegerField()

    def __unicode__(self):
        return self.member.first_name + " " + self.member.last_name + " " + \
            ", "+ self.get_month_display() + " -- " + str(self.amount)

    def save(self, *args, **kwargs):
        self.week_number = get_week_number(datetime.datetime.today())
        return super(Tithe, self).save(*args, **kwargs)
