"""autoload_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

admin.site.site_header = "Slide Presentation Admin"
admin.site.site_title = "Slide Presentation Admin Portal"
admin.site.index_title = "Welcome to Slide Presentation Portal"

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', include('homepage.urls')),
    #path('admin/', admin.site.urls),
    #url(r'^main/', include('main.urls'), namespace='Main'),
    url(r'^slide/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
]
