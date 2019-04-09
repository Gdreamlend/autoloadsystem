from django.contrib import admin
from .models import Slide
from .models import Department

class SlideAdmin(admin.ModelAdmin):
    list_display = ('department','file','monitor','start_date','end_date','priority', 'description','status')
    list_display_links = ['department']
    list_editable = ['monitor','priority', 'start_date', 'end_date','status']
    search_fields = ['monitor', 'status','department']

admin.site.register(Slide, SlideAdmin)
admin.site.register(Department)
