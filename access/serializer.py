from rest_framework import serializers as ser
from .models import FormtwoResponses
class MyData(ser.ModelSerializer):
    class Meta:
        model = FormtwoResponses
        exclude=('')