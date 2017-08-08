from django.db import models

class EventCalendar(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    location = models.CharField(max_length=200)

class RecurringEventCalendar(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    day = models.IntegerField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    
    location = models.CharField(max_length=200)
