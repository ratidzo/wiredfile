from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="school"
    )
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
