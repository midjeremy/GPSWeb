from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet
from .views import gps_view

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', gps_view, name='gps'),
]
