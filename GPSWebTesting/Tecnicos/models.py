from django.db import models

# Create your models here.
class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    class meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.especialidad})"
