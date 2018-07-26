
from django import forms
from .models import Word, Student


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "words"]
    words = forms.ModelMultipleChoiceField(queryset=Word.objects.all(), widget=forms.CheckboxSelectMultiple,)
    #     words = forms.ModelMultipleChoiceField(queryset=Word.objects.all(), widget=forms.CheckboxSelectMultiple,)

# class WordForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'manager']
#         widgets = {
#             'manager': forms.Select(),
#         }
#     student = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
#     words = forms.ModelMultipleChoiceField(queryset=Word.objects.all(), widget=forms.CheckboxSelectMultiple,)
#
#     def __init__(self, *args, **kwargs):
#         super(WordForm, self).__init__(*args, **kwargs)
#         self.fields['words'].queryset = Word.objects.all()
#
# class WordForm(forms.ModelForm):
#     words = forms.ModelMultipleChoiceField(queryset= Word.objects.all(), required=False)
#
#     class Meta:
#         model = Student
#         fields = ['first_name', 'words']
#         widgets = {
#             'words': forms.Select(),
#         }
# class StudentModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return obj.get_full_name()
#
#
# class WordForm(forms.ModelForm):
#     words = StudentModelChoiceField(queryset=Word.objects.all(), label='words', required=True)
#
#     class Meta:
#         model = Student
#         fields = ['first_name']

#
# class WordForm(forms.ModelForm):
#     words = forms.ModelMultipleChoiceField(queryset=Word.objects.all())
#     class Meta:
#         model = Student
#         fields = ["first_name"]
#         widgets = {"words":forms.Select(),}

# class WordForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields= ["first_name", "last_name"]
#         widgets = {"words":forms.Select(),}
#
#
#     words = forms.ModelMultipleChoiceField(queryset=Word.objects.all())
#     #
#     def __init__(self, *args, **kwargs):
#
#         if kwargs.get('instance'):
#             initial = kwargs.setdefault('initial', {})
#             initial['words'] = [t.pk for t in
#                 kwargs['instance'].words.all()]
#
#         forms.ModelForm.__init__(self, *args, **kwargs)
#
#     def save(self, commit=True):
#         instance = forms.ModelForm.save(self, False)
#         old_save_m2m = self.save_m2m
#
#         def save_m2m():
#             old_save_m2m()
#             instance.words.clear()
#             for word in self.cleaned_data['words']:
#                 instance.words.add(word)
#
#             self.save_m2m = save_m2m
#             instance.save()
#             self.save_m2m()
#
#         return instance



# # Create a form instance with POST data.
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

    #
    # def addBook(request):
    #     if request.method == 'POST':
    #         form = WordForm(request.POST)
    #         if form.is_valid():
    #             newbook = form.save(commit=False)
    #             newbook.save()
    #             newbook.user.add(uId)
    #             form.save_m2m()
    #     else:
    #         form = AddBook()
    #         context = {
    #         'addForm': form,
    #         }
    #     return render(request, 'books/base_books_addBooks.html', context)

    # def clean(self):
    #     cleaned_data = super(WordForm, self).clean()
    #     return self.cleaned_data
    #
    # def save(self, commit=True):
    #     student = super(WordForm, self).save(commit=False)
    #     if commit:
    #         student.save()
    #         self.save_m2m()
    #     return student
        # word.student_set.add(self.object)

# class WordForm(forms.ModelForm):
#     class Meta:
#         model = Word
#         fields = ['word']
#         students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.CheckboxSelectMultiple())
#
#     def __init__(self, *args, **kwargs):
#         if kwargs.get('instance'):
#             initial = kwargs.setdefault('initial', {})
#             initial['students'] = [t.pk for t in kwargs['instance'].student_set.all()]
#
#         forms.Form.__init__(self, *args, **kwargs)
#
#
#     def save(self, commit=True):
#         instance = forms.Form.save(self, False)
#         old_save_m2m = self.save_m2m
#         def save_m2m():
#            old_save_m2m()
#            instance.student_set.clear()
#            for student in self.cleaned_data['students']:
#                instance.student_set.add(student)
#         self.save_m2m = save_m2m
#
#         if commit:
#             instance.save()
#             self.save_m2m()
#
#         return instance
