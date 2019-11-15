from django.urls import path, include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('', views.Profileview)

urlpatterns = [
path('homepage/',views.homepage,name='homepage'),
path('assesment/',views.scorecard,name='assesment'),
path('rejected/',views.failed,name='rejected'),
path('accepted/',views.failed,name='accepted'),
]