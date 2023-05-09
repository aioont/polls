from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    mobile_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter a valid mobile number.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'mobile_number', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
