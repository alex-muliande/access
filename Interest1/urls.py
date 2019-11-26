from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
        path('congrats/',views.congragulate2),
        path('interest/',views.homepage,name='interest'),
        path('interestaccepted/',views.firststageaccepted,name='interestaccepted'),
        path('rejected/',views.rejected),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

