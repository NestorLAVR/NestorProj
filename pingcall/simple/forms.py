from django import forms
from . models import FirstParametr, Visualize, SecondParametr

class UserForm(forms.Form):

    choose1 = forms.ModelChoiceField(queryset=FirstParametr.objects.order_by('name'), required=False, initial=None)

    choose2 = forms.ModelChoiceField(queryset=SecondParametr.objects.order_by('name'), required=False, initial=None )

    choose_Visualization = forms.ModelChoiceField(queryset=Visualize.objects.order_by(('-id')), required=False,
                                                  initial=Visualize.objects.first())