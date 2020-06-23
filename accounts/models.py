from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(_('Full name'), max_length=30, blank=True)
    email = models.EmailField(_('Email'), unique=True)
    phone_number=models.CharField(_('Phone Number'), unique=True,max_length=20)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff'), default=True) 
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

