from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

LOGIN_FORM_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs= {
    'placeholder': 'Your username',
    'class': LOGIN_FORM_CLASSES
  }))
  password = forms.CharField(widget=forms.PasswordInput(attrs= {
    'placeholder': 'Your password',
    'class': LOGIN_FORM_CLASSES
  }))

class SignUpForm(UserCreationForm):
  class Meta:
      model = User
      fields = ("username", "email", "password1", "password2")

  username = forms.CharField(widget=forms.TextInput(attrs= {
     'placeholder': 'Your username',
     'class': LOGIN_FORM_CLASSES
  }))
  email = forms.CharField(widget=forms.TextInput(attrs= {
     'placeholder': 'Your email address',
     'class': LOGIN_FORM_CLASSES
  }))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
     'placeholder': 'Your password',
     'class': LOGIN_FORM_CLASSES
  }))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs= {
     'placeholder': 'Repeat password',
     'class': LOGIN_FORM_CLASSES
  }))
