from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^login/$', views.LoginPageView.as_view(), name='login'),
    url(r'^signup/$', views.SignupPageView.as_view(), name='signup'),
]
