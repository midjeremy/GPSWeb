from django.db import models

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.updated_at}"

    