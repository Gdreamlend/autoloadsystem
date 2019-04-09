from django.shortcuts import render
from homepage.forms import SlideForm
from django.views.generic import TemplateView


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
            #text = form.cleaned_data['form']
            form = SlideForm()

            return render(request, "submitted.html", locals())
        else:
            form = SlideForm()
            return render(request, self.template_name, {'form': form})
class SubmittedPageView(TemplateView):
    template_name = "submitted.html"

