from django import forms
from .models import InitialForm,Try

class InitialformCreateView(forms.ModelForm ):
    class Meta:
        model = InitialForm
        fields = ['cert_image','name','email']

class FormsTry(forms.ModelForm):
    class Meta:
        model = Try
        fields = ['name','email','age']