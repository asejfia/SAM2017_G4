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
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Paper(models.Model):
    formatChoices = (
        ('PDF', 'PDF'),
        ('Word', 'Word'),
    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    version = models.FloatField()
    paper = models.FileField(upload_to='documents/')
    formats = models.CharField(max_length=5, choices=formatChoices)  # find the enumerate field for word and PDF
    rate = models.FloatField(default=None, null=True)
    sub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
