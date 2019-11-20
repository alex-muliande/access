from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import InitialformCreateView
#router = routers.DefaultRouter()
#router.register('', views.Profileview)



urlpatterns=[
    path('', views.index, name ='index'),
    path('initial/',views.initial, name='initial'),
    path('bulk/',views.congragulate),
    path('congrats/',views.congragulate2),
    path('congrats3/',views.congragulate3),
    path('congrats4/',views.congragulate4),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

