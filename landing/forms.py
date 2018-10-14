from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address_1', 'address_2', 'city', 'state', 'zipcode')
