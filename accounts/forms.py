from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args,**kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email Address"


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         fields = ("username", "email", "password1", "password2")
#         model = get_user_model()
