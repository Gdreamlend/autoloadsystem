from django.shortcuts import render
from homepage.forms import SlideForm
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
#views
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
class AboutPageView(TemplateView):
    template_name = "about.html"
class RequestPageView(TemplateView):
    template_name = "request.html"

    def get(self, request):
        form = SlideForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form = SlideForm()
            email_address = 'jiangshanyigou@gmail.com'
            email = EmailMessage('New Slide Application', 'You have a new application', to=[email_address])
            email.send()
            return render(request, "submitted.html", locals())
        else:
            form = SlideForm()
            messages.error(request, "Submit failed, Change error inputs please")
            return render(request, self.template_name, {'form': form})
class SubmittedPageView(TemplateView):
    template_name = "submitted.html"

