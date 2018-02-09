from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
