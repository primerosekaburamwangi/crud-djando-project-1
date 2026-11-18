# app - models.py file

from django.contrib.auth.hashers import (
    check_password,
    make_password,
)
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="uploads", default="a.png")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
