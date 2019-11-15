from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import InitialformCreateView
from . import views

urlpatterns=[
    path('', views.index, name ='index'),

    path('initial/', InitialformCreateView.as_view(), name='initial'),
    path('forms', views.myforms, name ='forms'),
    path('get_data/',views.StageOne),
    path('final/',views.FinalList),
    path('initial/',views.initial, name='initial'),
    path('bulk/',views.congragulate)

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

