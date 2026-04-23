from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # noqa


admin.site.site_header = "Pulse Attendance System Admin"
admin.site.site_title = "Pulse Admin Portal"
admin.site.index_title = "Welcome to Pulse Attendance System Admin Portal"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
