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
from forms import student_form

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

#
# def wordform(request):
#     form = forms.WordForm()
#     if form.is_valid():
#             wordform = form.save(commit=False)
#             wordform.save()
#             form.save_m2m()
#             success_url = reverse_lazy('students:index')
#     return render(request, "students/formpage.html", {"form": form})
#


# def wordform(request):
#     if request.method == "POST":
#         form = WordForm(request.POST)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.user = request.user
#             student.save()
#             students= Student.objects.filter()
#             return render(request, "students/index.html", {"form": form})
#     else:
#         form = WordForm()
#         # print("Else")
#     return render(request, "students/formpage.html", {'form': form})

# class StudentUpdate(UpdateView):
#     model = Student
#     form_class = WordForm

def student_edit(request, objectid):
    # link = 'Student'
    student_inst = Student.objects.get(id=objectid)
    form = student_form(instance=student_inst)

    if request.method == 'POST':
        f = student_form(request.POST, instance=student_inst)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/student')
    return render(request, "student_edit.html",
                  {"form": form})

#
#
#     if request.method == 'POST':
#         form = WordForm(request.POST)
#         if form.is_valid():
#         # get cleaned data from form
#             student_name = form.cleaned_data['first_name']
#             student_words = form.cleaned_data['words']  # this is a User-object
#
#         # generate project and store it to db
#             student = student(name=student_name)
#             student.save()
#
#         # handling now m2m relation for manager
#             student.words.add(student_words)
#
#             return render(request, "students/formpage.html", {"form": form})
#
#         else:
#             form = WordForm()
#
#
# def wordform(request, pk):
#     student=get_object_or_404(Student, pk = pk)
#
#     # If this is a POST request then process the Form data
#     if request.method == 'POST':
#
#         # Create a form instance and populate it with data from the request (binding):
#         form = WordForm(request.POST)
#
#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             student.words = form.cleaned_data['renewal_date']
#             student.save()
#
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('all-borrowed') )
#
#     # If this is a GET (or any other method) create the default form.
#
#     return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
# #
# def wordform(request):
#         f = WordForm(request.POST)
#
# # Create, but don't save the new author instance.
#         new_student = f.save(commit=False)
#
# # Modify the author in some way.
#         new_student.words = 'words'
#
# # Save the new instance.
#         new_student.save()
#
# # Now, save the many-to-many data for the form.
#         f.save_m2m()
    # form = forms.WordForm()
    # if form.is_valid():
    #         wordform = form.save(commit=False)
    #         wordform.save()
    #         wordform.save_m2m()
    #         success_url = reverse_lazy('students:index')
    # return render(request, "students/formpage.html", {"form": form})
