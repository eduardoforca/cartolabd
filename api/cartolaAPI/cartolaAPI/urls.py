"""cartolaAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.authtoken import views as ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/usuarios/', include('api.urls', namespace='crud_usuario')),
    path('v1/autorizar/', ObtainAuthToken.obtain_auth_token, name='autorizar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
