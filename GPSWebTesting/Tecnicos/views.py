#████████████[Librerias]████████████
from django.shortcuts import render, redirect, get_list_or_404
from .models import Tecnico
from .forms import TecnicoForm

#████████████[Vistas]████████████
#Vista de html
def empleado(request):
    return render(request, 'empleado.html')

#Listar
def lista_Tecnico(request):
    tecnicos = Tecnico.objects.all()
    return render (request, 'empleado.html', {'tecnicos': tecnicos})

#Añadir

#Editar

#Eliminar