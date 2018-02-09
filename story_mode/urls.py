from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include

from personae.views import user_profile, create_persona

urlpatterns = [
    # personae
    path('user/profile/', user_profile, name='user_profile'),
    path('persona/create/', create_persona, name='create_persona'),

    # django-allauth
    path('auth/', include('allauth.urls')),

    # django.contrib.admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.contrib.staticfiles.views import serve

    urlpatterns.append(re_path(r'^(?P<path>favicon\.ico|robots\.txt)$', serve))
