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
    list_display = ('department','thumbnail','start_date','end_date','status')
    list_display_links = ['department']
    list_editable = [ 'start_date', 'end_date','status']
    search_fields = [ 'status','department']

    actions = [make_approved, make_rejected]



    def thumbnail(self, obj):
        url = "http://slideshow.ml/autoload_system/slide/"
        if obj.file:
            url = url + str(obj.file)

            # return format_html('<img src= "https://view.officeapps.live.com/op/embed.aspx?src=[{}]" style="width: 130px; \
            #                             height: 100px" />'.format(url))

            return format_html('<iframe id = "iframe1" src = "http://docs.google.com/gview?url={}&embedded=true" \
                onload = "javascript:this.contentWindow.location.hash=":0.page.20"; style="width: 130px; \
            #                             height: 100px"></iframe>'.format(url))
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
