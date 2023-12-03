from django.db import models
from datetime import datetime

today = datetime.now()


class UserClass(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
