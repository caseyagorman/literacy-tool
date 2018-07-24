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

User= get_user_model()

# def index(request):
#     if request.user.is_authenticated():
#         all_students = Student.objects.filter(user=request.user)
#         return render(request, 'students/index.html')
#


class IndexView(generic.ListView):
    model = Student
    template_name= "students/index.html"
    context_object_name = "all_students"
    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)
#
#     Student.objects.filter(owner__in=self.request.user.all())
#     # def get_queryset(self):
#     #     try:
    #         self.student.user = User.objects.prefetch_related("students").get(user=self.kwargs.get('user'))
    #     except User.DoesNotExist:
    #         raise Http404
    #     else:
    #         return self.student_user.students.all()

# class IndexView(LoginRequiredMixin, generic.ListView):
#     template_name = "students/index.html"
#     context_object_name = "all_students"
#
#     def get_queryset(request):
#         if request.user.is_authenticated():
#             all_students = Student.objects.filter(user=request.user)
#
# class IndexView(LoginRequiredMixin, ListView):
#     queryset = Student.objects.all()
#
#     def get_queryset(self,request):
#     try:
#
#         student = Student.objects.get(email=user_check_email)
#         return super(OrderList, self).get_queryset().filter(user=user_checkout)
#     except ObjectDoesNotExist:
#         return render(request, 'no_orders.html')

class DetailView(generic.DetailView):
    model = Student
    template_name = "students/student_detail.html"
#
# @login_required
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         exclude = ['user', ]
#
# def task_create(request):
#     form = TaskForm(data=request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         task = form.save(commit=False)
#         task.user = request.user
#         task.save()
#         return reverse("todo_list")
#     return render(request,
#         'task_create.html',
#         {'form': form}
#     )


@method_decorator(login_required, name="dispatch")
class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields =['first_name', 'last_name', 'grade']

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super(StudentCreate, self).form_valid(form)

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


class WordCreate(CreateView):
    model = Word
    fields = ['word']

@method_decorator(login_required, name="dispatch")
class WordCreate(LoginRequiredMixin, CreateView):
    model = Word
    fields =['word']

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super(StudentCreate, self).form_valid(form)

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(WordCreate, self).form_valid(form)

class WordDelete(DeleteView):
    model = Word
    success_url = reverse_lazy('students:word_index')
