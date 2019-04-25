from django import forms
from homepage.models import Slide
from django.contrib.admin import widgets


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ('department','email', 'monitor', 'start_date','end_date','file', 'description')
        start_date = forms.DateField(widget=forms.SelectDateWidget())
        end_date = forms.DateField(widget=forms.SelectDateWidget())

        def __init__(self, *args, **kwargs):
            super(SlideForm, self).__init__(*args, **kwargs)
            self.fields['date'].widget = widgets.AdminDateWidget()
            self.fields['start_date'].widget = widgets.AdminTimeWidget()
            self.fields['end_date'].widget = widgets.AdminTimeWidget()