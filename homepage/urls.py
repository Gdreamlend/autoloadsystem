from django.conf.urls import url
from homepage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^request/$', views.RequestPageView.as_view()),
    url(r'submitted/$', views.SubmittedPageView.as_view()),

]