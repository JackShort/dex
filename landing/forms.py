from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
    
    def clean_username(self):
        username = self.cleaned_data['username']

        if not username.isalpha():
            raise forms.ValidationError("Please only alphanumeric symbols")
        
        return username

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address_1', 'address_2', 'city', 'state', 'zipcode')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['address_2'].required = False

    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        if len(zipcode) != 5:
            raise forms.ValidationError("Not 5 digits")
        try:
            value = int(zipcode)
        except ValueError:
            raise forms.ValidationError("Only digits please")
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
								

