# Importamos path. 
from django.urls import path 
# Importamos nuestras vistas. 
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    #Direccion/registro/ 
    path( 
        'registro/', 
        views.registro, 
        name='registro' 
        ),
    # Login
    path( 
        'login/', 
        LoginView.as_view( 
            template_name='usuarios/login.html' 
            ), 
            name='login' 
        ),
    # Bienvenida
    path( 
        'bienvenida/', 
        views.bienvenida, 
        name='bienvenida' 
    ),
    ]