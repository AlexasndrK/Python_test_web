from django.conf.urls import url
from djangoApp import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^help', views.help, name='help'),
    url(r'^test', views.testHtml, name='test'),
    url(r'^users', views.users, name='users'),
]
