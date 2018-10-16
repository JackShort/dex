from django.contrib.auth.models import User
from django import forms
from .models import Profile

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