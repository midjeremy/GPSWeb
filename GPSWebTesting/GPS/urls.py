from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, RouteViewSet
from .views import gps_view

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'routes', RouteViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', gps_view, name='gps'),
]
