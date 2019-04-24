from django.contrib import admin
from .models import Slide
from .models import Department
from django.utils.html import format_html
from django.core.mail import EmailMessage
from django.conf import settings

def make_approved(modeladmin, request, queryset):
    queryset.update(status='approved')
    for apply in queryset:
        email_address = apply.email
        email = EmailMessage('Slide Application', 'Your application has been approved', to=[email_address])
        email.send()
make_approved.short_description = "Approve all selected"

def make_rejected(modeladmin, request, queryset):
    queryset.update(status='rejected')

    for apply in queryset:
        email_address = apply.email
        email = EmailMessage('Slide Application', 'Your application has been rejected', to=[email_address])
        email.send()
make_rejected.short_description = "Reject all selected"



class SlideAdmin(admin.ModelAdmin):
    list_display = ('department','thumbnail','monitor','start_date','end_date','priority', 'description','status')
    list_display_links = ['department']
    list_editable = ['monitor','priority', 'start_date', 'end_date','status']
    search_fields = ['monitor', 'status','department']

    actions = [make_approved, make_rejected]



    def thumbnail(self, obj):
        url = "http://40.113.220.78/autoload_system/slide/"
        if obj.file:
            url = url + str(obj.file)
            # return u'<img src="%s" />' % url
            return format_html('<img src="{}" style="width: 130px; \
                                        height: 100px"/>'.format(url))
        else:
            return '(No image found)'

    thumbnail.short_description = 'thumbnail'
    thumbnail.allow_tags = True

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)
        if obj.status == "approved":
            email_address = obj.email
            email = EmailMessage('Slide Application', 'Your application has been approved', to=[email_address])
            email.send()
        elif obj.status == "rejected":
            email_address = obj.email
            email = EmailMessage('Slide Application', 'Your application has been rejected, the reason is: '+ obj.reject_info, to=[email_address])
            email.send()


admin.site.register(Slide, SlideAdmin)
admin.site.register(Department)
