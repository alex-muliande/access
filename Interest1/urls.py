from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
        #path('congrats/',views.congragulate2),
        path('loader/',views.loaderpage,name='loader'),
        path('loader/interest/',views.homepage,name='interest'),
        path('loader2/',views.loader2page,name='loader2'),
        path('loader2/interestaccepted/',views.firststageaccepted,name='loader2/interestaccepted'),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

