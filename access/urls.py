from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import InitialformCreateView
from . import views 

#router = routers.DefaultRouter()
#router.register('', views.Profileview)



urlpatterns=[
    path('', views.index, name ='index'),
    path('forms', views.myforms, name ='forms'),
    path('get_data/',views.StageOne),
    path('final/',views.FinalList),
    path('initial/',views.initial, name='initial'),
    path('more/',views.KnowMore,name = 'more'),
    path('assesment/',views.scorecard,name='assesment'),
    path('rejected/',views.failed,name='rejected'),
    path('accepted/',views.failed,name='accepted'),
    path('bulk/',views.congragulate),
    path('congrats/',views.congragulate2),
    path('congrats3/',views.congragulate3),
    path('congrats4/',views.congragulate4),
    path('congrats5/',views.more),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

