from django import forms
from homepage.models import Slide


# FRUIT_CHOICES= [
#     ('First Floor Lobby', 'First Floor Lobby'),
#     ('Second Floor Lobby', 'Second Floor Lobby'),
#     ('Second Floor Office', 'Second Floor Office'),
#     ]


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ('department','email', 'monitor', 'start_date','end_date','file', 'description')
    #monitor = favorite_fruit= forms.CharField(label='Where do you want to put your slide?', widget=forms.Select(choices=FRUIT_CHOICES))
    #email= forms.CharField()
    #department = forms.CharField()
    #description = forms.CharField()
    #start_date = forms.DateField(widget=forms.TextInput(attrs=
    #                            {
    #                                'class':'datepicker'
    #                            }))
    #end_date = forms.DateField(widget=forms.TextInput(attrs=
    #                            {
    #                                'class':'datepicker'
     #                           }))
    #file = forms.CharField()
