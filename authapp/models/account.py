from django.db import models
from .user import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account')
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)