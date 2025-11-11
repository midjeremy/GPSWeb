from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    error = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if user.role == 'supervisor':
                    return redirect('SuperUsuario')
                else:
                    return redirect('dashboard_tecnico')
            else:
                error = 'Credenciales incorrectas'
    return render(request, 'login.html', {'form': form, 'error': error})
