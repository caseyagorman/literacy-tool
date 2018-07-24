# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic, View
from students.models import Student, Word
from accounts.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.forms import SelectMultiple, ModelForm
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from . import forms
from braces.views import SelectRelatedMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from forms import WordForm

User= get_user_model()


class IndexView(generic.ListView):
    model = Student
    template_name= "students/index.html"
    context_object_name = "all_students"
    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)

class DetailView(generic.DetailView):
    model = Student
    template_name = "students/student_detail.html"

@method_decorator(login_required, name="dispatch")
class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields =['first_name', 'last_name', 'grade']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(StudentCreate, self).form_valid(form)

class StudentUpdate(UpdateView):
    model = Student
    fields =['first_name', 'last_name', 'grade']

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students:index')

class WordListView(generic.ListView):
    model = Word
    template_name= "students/word_index.html"
    context_object_name = "all_words"

    def get_queryset(self):
        return Word.objects.filter(user=self.request.user)

class WordDetailView(generic.DetailView):
    model = Word
    template_name = "students/word_detail.html"


@method_decorator(login_required, name="dispatch")
class WordCreate(LoginRequiredMixin, CreateView):
    model = Word
    fields =['word']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(WordCreate, self).form_valid(form)

class WordDelete(DeleteView):
    model = Word
    success_url = reverse_lazy('students:word_index')

def wordform(request):
    form = forms.WordForm()
    if form.is_valid():
            wordform = form.save(commit=False)
            wordform.save()
            wordform.save_m2m()
            success_url = reverse_lazy('students:index')
    return render(request, "students/formpage.html", {"form": form})
