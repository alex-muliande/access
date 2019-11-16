from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import InitialformCreateView
from . import views 
#router = routers.DefaultRouter()
#router.register('', views.Profileview)



urlpatterns=[
    path('', views.index, name ='index'),
    # path('initial/', InitialformCreateView.as_view(), name='initial'),
    path('forms', views.myforms, name ='forms'),
    path('get_data/',views.StageOne),
    path('final/',views.FinalList),
    path('initial/',views.initial, name='initial'),
    path('assesment/',views.scorecard,name='assesment'),
    path('rejected/',views.failed,name='rejected'),
    path('accepted/',views.failed,name='accepted'),
    path('bulk/',views.congragulate)

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

