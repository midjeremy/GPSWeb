from django.shortcuts import render

# Create your views here.
def empleado(request):
    return render(request, 'empleado.html')