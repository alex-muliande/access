from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import InitialformCreateView


#router = routers.DefaultRouter()
#router.register('', views.Profileview)

urlpatterns = [
path('', views.index, name ='index'),
path('initial/',views.initial, name='initial'),
path('bulk/',views.congragulate),
path('assesment/',views.scorecard,name='assesment'),
path('rejected/',views.failed,name='rejected'),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

