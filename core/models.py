from django.db import models
from datetime import date, time , datetime
from django.utils.timezone import now
from django.contrib.auth.models import User

class Userdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Usernote(models.Model):
    userdate = models.ForeignKey(Userdate, on_delete=models.CASCADE, null= True, blank=True)
    time = models.TimeField(null=True, blank=True)
    task = models.CharField(max_length=1500, null=True , blank= True)
    isdone = models.BooleanField(default=False) 