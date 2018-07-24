# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import auth

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.uesrname

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
# Create your models here.
