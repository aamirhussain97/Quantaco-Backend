from django.db import models

class UserDetails(models.Model):
    firstName = models.CharField(max_length=100, default=None)
    lastName = models.CharField(max_length=100, default=None)
    dob = models.DateField(default=None)
    phoneNumber = models.CharField(max_length=15, default=None)
