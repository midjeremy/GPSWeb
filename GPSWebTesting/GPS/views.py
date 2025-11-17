import requests
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer
from django.shortcuts import render

def gps_view(request):
    return render(request, 'gps.html')

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('-updated_at')
    serializer_class = LocationSerializer

    def geocode(self, address):
            """Convierte una dirección en coordenadas usando Nominatim."""
            url = "https://nominatim.openstreetmap.org/search"
            params = {
                'q': address,
                'format': 'json',
                'limit': 1
            }
            headers = {"User-Agent": "django-app"}
            response = requests.get(url, params=params, headers=headers)
            data = response.json()

            if not data:
                return None
            
            return {
                "latitude": float(data[0]["lat"]),
                "longitude": float(data[0]["lon"])
            }

    @action(detail=False, methods=['post'])
    def route(self, request):
        """Recibe una direccion de inicio y destino y devuelve las coordenadas."""
        start_address = request.data.get("start_address")
        end_address = request.data.get("end_address")

        if not start_address or not end_address:
                return Response(
                    {"error": "Debes enviar start_address y end_address"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        start_coords = self.geocode(start_address)
        end_coords = self.geocode(end_address)

        if not start_coords or not end_coords:
            return Response(
                {"error": "No se pudieron encontrar coordenadas"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({
            "start": start_coords,
            "end": end_coords
        }, status=status.HTTP_200_OK)