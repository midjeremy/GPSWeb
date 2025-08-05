from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer
from django.shortcuts import render

def gps_view(request):
    return render(request, 'gps.html')

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('-updated_at')
    serializer_class = LocationSerializer

