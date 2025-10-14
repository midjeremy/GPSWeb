from django.shortcuts import render

# Create your views here.
def SuperU(request):
    return render(request, 'usuarioSuper.html')