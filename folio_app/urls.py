from django.urls import include, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
     path('contact/', contact_view, name='contact'),
    path('contact/success/',contact_success_view, name='contact_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)