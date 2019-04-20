from django.contrib import admin
from .models import Slide
from .models import Department
from django.utils.html import format_html
from django.utils.safestring import mark_safe

def make_approved(modeladmin, request, queryset):
    queryset.update(status='approved')
make_approved.short_description = "Approve all selected"

def make_rejected(modeladmin, request, queryset):
    queryset.update(status='rejected')
make_rejected.short_description = "Reject all selected"



class SlideAdmin(admin.ModelAdmin):
    list_display = ('department','thumbnail','monitor','start_date','end_date','priority', 'description','status')
    list_display_links = ['department']
    list_editable = ['monitor','priority', 'start_date', 'end_date','status']
    search_fields = ['monitor', 'status','department']

    actions = [make_approved, make_rejected]

    def thumbnail(self, obj):
        url = "http://40.113.220.78/autoload_system"
        if obj.file:
             url = url + str(obj.file)

        return u'<img src="%s"  style="width: 130px; \
                            height: 100px"/>' % url
    thumbnail.short_description = 'thumbnail'

    # def thumbnail(self, obj):
    #     if obj.file:
    #         return u'<img src="%s" />
    #     else:
    #         return '(No image found)'
    #
    # thumbnail.short_description = 'thumbnail'
    # thumbnail.allow_tags = True
    # def thumbnail(self, obj):
    #     if obj.file:
    #         return mark_safe('<img src="%s"  height="100px"/>' % obj.file)
    #     else:
    #         return 'No_image'
    #     thumbnail.short_description = 'thumbnail'
    #     thumbnail.allow_tags = True

admin.site.register(Slide, SlideAdmin)
admin.site.register(Department)
