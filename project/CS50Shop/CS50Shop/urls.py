from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

from CS50Shop import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ShopDegenerative.urls', namespace="ShopDegenerative")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
