"""
URL configuration for GPSWebTesting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from Tecnicos.views import empleado
#from Supervisor.views import 
from Supervisor.views import SuperU
#from Tecnicos.views import 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('gps/', include('GPS.urls')),
    #path('', include('login.urls')),
    path('', include('accounts.urls')),
    #path('', login, name="iniciar sesion"), #Pestaña de inicio de sesion
    path('menu_empleado/', empleado, name = "Menu"), #MENÚ DEL EMPLEADO
    #path('registrar/', register, name="registrar"), #Añadir registro
    path('Supervisor/', SuperU, name="SuperUsuario"), #Añadir Views de Supervisor
    #path('GPS/', include('GPS.urls'), name=""), #Añadir GPS.
    #path ('/', , name=""), #Añadir view de tecnicos
]

