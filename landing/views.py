from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
