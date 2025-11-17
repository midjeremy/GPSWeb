#████████████[Librerias]████████████
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnico
from .forms import TecnicoForm

#████████████[Vistas]████████████
#Vista de html
def empleado(request):
    return render(request, 'reportes.html')

#Listar
def lista_Tecnico(request):
    tecnicos = Tecnico.objects.all()
    return render (request, 'empleado.html', {'tecnicos': tecnicos})

#Añadir
def Add_Tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_Tecnico')
        else:
            form = TecnicoForm()
        return render (request, "tecnicos/forms.html", {'form': form, 'titulo': "añadir tecnico"})
#Editar
def edit_Tecnico (request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    if request.method == "POST":
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return
        redirect("lista_Tecnicos")
    else:
        form = TecnicoForm(instance=tecnico)
        return render(request,"tecnicos/form.html", {'form': form, 'titulo': 'editar tecnico'})
#Eliminar
def borrar_Tecnico (request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    tecnico.delete()
    return redirect('lista_Tecnico')