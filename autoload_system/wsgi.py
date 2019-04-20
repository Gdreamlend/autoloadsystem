"""
WSGI config for autoload_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autoload_system.settings')
sys.path.append('/opt/bitnami/apps/django/django_projects/autoload_system')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/autoload_system/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autoload_system.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
