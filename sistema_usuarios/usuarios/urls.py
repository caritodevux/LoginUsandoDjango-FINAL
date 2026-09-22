# Importamos path. 
from django.urls import path 
# Importamos nuestras vistas. 
#from django.contrib.auth.views import LoginView
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

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
    # Editar perfil
    path(
        'editar-perfil/',
        views.editar_perfil,
        name='editar_perfil'
    ),
    # Eliminar perfil
    path(
        'eliminar-cuenta/',
        views.eliminar_cuenta,
        name='eliminar_cuenta'
    ),
    #LoginView
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    ]