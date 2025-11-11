from django import forms
from .models import Tecnico

class TecnicoForm(forms.ModelForm):
    model = Tecnico
    fields = ["nombre","apellido", "rut", "telefono", "email", "especialidad"]