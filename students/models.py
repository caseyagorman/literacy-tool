# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.text import slugify
from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db.models import CharField, Model
from accounts.models import User
from django.contrib import auth

User = get_user_model()

from django import template
register = template.Library()


class Word(models.Model):
    word = models.CharField(max_length=250, default= "", blank=True)
    user = models.ForeignKey('auth.User', default= "")

    def get_absolute_url(self):
        return reverse('students:word_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.word

class Student(models.Model):
    user = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=250, default="", blank=True)
    last_name = models.CharField(max_length=250, default="", blank=True)
    grade = models.CharField(max_length=5, default="", blank=True)
    words = models.ManyToManyField(Word, default="", blank=True)

    def get_absolute_url(self):
        return reverse('students:student_detail', kwargs={'pk':self.pk})
    # word = models.ForeignKey(Word, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name
