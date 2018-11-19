from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
   	url(r'^subscribe/$', views.SubscribePageView.as_view(), name='subscribe'),
   	url(r'^select/$', views.SelectPageView.as_view(), name='select'),
   	url(r'^pay/$', views.PayPageView.as_view(), name='pay'),
   	url(r'^member/$', views.member, name='member'),
   	url(r'^signout/$', views.signout, name='signout'),
   	url(r'^change_password/$', views.change_password, name='change_password'),
   	url(r'^change_plan/$', views.change_plan, name='change_plan'),


]
