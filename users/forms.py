from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
