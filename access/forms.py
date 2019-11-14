from django import forms
from .models import InitialForm

class InitialformCreateView(forms.ModelForm ):
    class Meta:
        model = InitialForm
        fields = ['KCSE_certificate_image','name','email']

