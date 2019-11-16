from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import InitialformCreateView
from . import views

urlpatterns=[
    path('', views.index, name ='index'),
    path('initial/',views.initial, name='initial'),
    path('bulk/',views.congragulate),
    # path('congrats/',views.congragulate2),
    # path('congrats2/',views.congragulate3)
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

