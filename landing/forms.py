from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address_1', 'address_2', 'city', 'state', 'zipcode')
    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        if zipcode != '5':
            raise forms.ValidationError("fuck you joe")
        return zipcode
    def clean_address_1(self):
       	address_1 = self.cleaned_data['address_1']
       	address_1 = address_1.replace(" ", "")
        if not address_1.isalnum():
        	raise forms.ValidationError("Please use only Alphanumeric characters in the Address box")
        return address_1
    def clean_city(self):
       	city = self.cleaned_data['city']
       	city = city.replace(" ", "")
        if not city.isalpha():
        	raise forms.ValidationError("Please use only letters in the City box")
        return city
								

