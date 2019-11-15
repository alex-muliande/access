from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('register/', views.register, name ='register'),
    path('', include("django.contrib.auth.urls")),
    path('django-sb-admin/', include('django_sb_admin.urls')),
    path('accounts/', include("django.contrib.auth.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
