from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[    
       
        path('loader3/',views.loader3page,name='loader3'),
        path('loader3/assesment/',views.scorecard,name='assesment'),
        path('congrats4/',views.congragulate4),
        path('rejected/',views.rejected),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

