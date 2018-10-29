from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.conf import settings

from .forms import UserForm, ProfileForm

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class SignupPageView(TemplateView):
    template_name = "signup.html"

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_profile = profile_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile.user = new_user
            new_profile.save()

            send_mail(
                'Welcome to Dex - Account Confirmation', # subject
                'Hi ' + user_form.cleaned_data['first_name'] + ', \n\n' # message
                    + 'Congratulations on succesfully registering for Dex, we\'re glad to have you! '
                    + 'Make sure you keep up date with the latest Dex news on our homepage and '
                    + 'look out for future emails with offers and other exclusives. Welcome to the '
                    + 'the future of web browsing. \n\n'
                    + 'Don\'t be afraid to reach out with any questions you may have,\n'
                    + 'The Dex Team',
                settings.EMAIL_HOST_USER, # email to send from
                [user_form.cleaned_data['email']] # recipient
            )

            login(request, new_user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            rawPassword = form.cleaned_data.get('password')
            user = authenticate (request, username=username, password=rawPassword)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
