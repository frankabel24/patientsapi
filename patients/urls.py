from rest_framework import routers
from .api import PatientViewSet
from .import views
from django.contrib import admin
from django.urls import include, path, re_path

router = routers.DefaultRouter()

router.register('api/patients', PatientViewSet, 'patients')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    re_path('api/login', views.login),
    re_path('api/register', views.register),
    re_path('api/profile', views.profile),    
    path('', include(router.urls)),
    ]

