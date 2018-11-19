from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import UserForm, ProfileForm, PlanForm
from .models import Profile

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

    def post(self, request, *args, **kwargs):
        context = request.POST
        if context['firstname'] != '' and context['lastname'] != '' and context['email'] != '' and context['content'] != '':

            send_mail(
                'Customer Contact from ' + context['firstname'], # subject
                'Customer First Name: ' + context['firstname'] + '\n' +
                'Customer E-Mail: ' + context['email'] + '\n' +
                'Customer Feedback: ' + context['content'],
                settings.EMAIL_HOST_USER, # email to send from
                [settings.EMAIL_HOST_USER] # recipient
            )
        
        return redirect('/')

class LoginPageView(TemplateView):
    template_name = "login.html"

class SignupPageView(TemplateView):
    template_name = "signup.html"

class SubscribePageView(TemplateView):
    template_name = "subscribe.html"

class SelectPageView(TemplateView):
    template_name = "select.html"

class PayPageView(TemplateView):
    template_name = "pay.html"

@login_required(login_url='/signin')
def signout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/signin')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
    
    return redirect('member')

@login_required(login_url='/signin')
def change_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST, request.user)
        if form.is_valid():
            new_plan = form.cleaned_data['plan']
            request.user.profile.plan = new_plan
            request.user.profile.save(update_fields=['plan'])
    
    return redirect('member')


@login_required(login_url='/signin')
def member(request):
    template_name = "member.html"
    password_form = PasswordChangeForm(request.user)
    plan_form = PlanForm(request.POST, request.user)
    plan_form.data = plan_form.data.copy()
    plan_form.data['plan'] = request.user.profile.plan

    return render(request, template_name, {
        'password_form': password_form,
        'plan_form': plan_form
    })

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('member')
        else:
            return render(request, 'signup.html', {'user_form': user_form})
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
                return redirect('member')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
