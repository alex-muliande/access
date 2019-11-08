from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import InitialformCreateView
#..............

urlpatterns=[

    path('initial/', InitialformCreateView.as_view(), name='initial')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  