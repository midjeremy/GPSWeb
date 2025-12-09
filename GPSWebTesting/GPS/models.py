from django.db import models

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    is_destination = models.BooleanField(default=False)  # NUEVO

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.updated_at}"

class Route(models.Model):
    start_lat = models.FloatField()
    start_lon = models.FloatField()
    end_lat = models.FloatField()
    end_lon = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ruta {self.id} - {self.created_at}"