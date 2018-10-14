from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

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
			user_form.save()
			profile_form.save()
			username = user_form.cleaned_data.get('username')
			rawPassword = user_form.cleaned_data.get('password')
			user = authenticate (username=username, password=rawPassword)
			login(request, user)
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
