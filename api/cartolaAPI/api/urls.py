from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

urlpatterns = [
    path('', views.ListCreateUsuarioAPIView.as_view(),name='create-list-usuario'),
    path('<int:id_usuario>/',views.GetUpdateRemoveUsuarioAPIView.as_view(), name='detail-usuario'),
]