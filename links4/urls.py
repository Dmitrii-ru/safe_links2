from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('site_link.urls')),
    path('registration/', include('users.urls')),
]
