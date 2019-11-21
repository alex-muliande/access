from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

path('forms/', views.myforms, name ='forms'),
path('final/',views.FinalList, name = 'final'),
path('get_data/',views.StageOne),
path('congrats3/',views.congragulate3),
path('update_status/<id>/' ,views.update_status,name='update_status')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  


