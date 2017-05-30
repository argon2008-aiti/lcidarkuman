from django.db import models
from info_system.models import Member

from django.contrib.auth.models import User

class Notice(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=2048)
    creator = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
