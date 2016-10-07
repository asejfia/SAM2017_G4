from django.db import models
from django.core.validators import RegexValidator
from django import forms
from django.forms import ModelForm
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class Author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=False)
    password_regex = RegexValidator(regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,50}$', message="Password must have at least 8 characters and must include at least one upper case letter, one lower case letter, and one numeric digit.")

    def __str__(self):
        return self.name