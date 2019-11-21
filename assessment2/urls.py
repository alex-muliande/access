from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[

        path('assesment/',views.scorecard,name='assesment'),
        path('rejected/',views.failed,name='rejected'),
        path('accepted/',views.failed,name='accepted'),
        path('congrats4/',views.congragulate4),



]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

