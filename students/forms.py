
from django import forms
from .models import Word, Student

class WordForm(forms.Form):
    student = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
    words = forms.ModelMultipleChoiceField(queryset=Word.objects.all(), widget=forms.CheckboxSelectMultiple,)

    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        self.fields['words'].queryset = Word.objects.all()

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
#         forms.ModelForm.__init__(self, *args, **kwargs)
#
#
#     def save(self, commit=True):
#         instance = forms.ModelForm.save(self, False)
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
