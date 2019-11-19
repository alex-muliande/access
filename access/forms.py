from django import forms
from .models import InitialForm,KnowMoringa

class InitialformCreateView(forms.ModelForm ):
    class Meta:
        model = InitialForm
        fields = ['KCSE_certificate_image','your_name','email']

class MoreInformation(forms.ModelForm):
    class Meta:
        model = KnowMoringa
        fields = ['name','email']
