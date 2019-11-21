from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

path('forms/', views.myforms, name ='forms'),
path('final/',views.FinalList),
path('get_data/',views.StageOne),
path('congrats3/',views.congragulate3)

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  


