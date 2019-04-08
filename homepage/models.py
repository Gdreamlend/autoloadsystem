from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
import os
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.file_address, filename)


class Slide(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to=get_file_path,default="")
    file_address = 'static/slide/'
    file_url = models.CharField(max_length=2000, default=file)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    status= models.CharField(max_length=2, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.department

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=200)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    role = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.id
