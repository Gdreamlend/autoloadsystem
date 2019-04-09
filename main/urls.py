# main/urls.py
from django.conf.urls import url
from main import views

app_name = 'main'

urlpatterns = [
    url("^$", views.LoginPageView.as_view()),
    url(r'^login/$', views.LoginPageView.as_view(), name='login'),
]