from django.db import models
from datetime import datetime

today = datetime.now()
date_of_birth = models.DateField()


class UserClass(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = today.year - int(date_of_birth)