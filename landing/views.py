from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

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
