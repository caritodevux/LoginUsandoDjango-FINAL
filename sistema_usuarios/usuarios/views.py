from django.shortcuts import render, redirect 
# Importamos nuestros formularios. 
from .forms import (
    RegistroUsuarioForm,
    EditarUsuarioForm,
)
from django.contrib.auth.decorators import login_required

# login_required significa que solamente 
# usuarios autenticados pueden acceder. 
@login_required 
def bienvenida(request): 
    return render( 
        request, 'usuarios/bienvenida.html' 
    )

# Vista responsable del registro. 
def registro(request): 
    # Comprobamos si el navegador está enviando información mediante POST. 
    if request.method == 'POST': 
        # Creamos un formulario utilizando la información recibida. 
        form = RegistroUsuarioForm(request.POST) 
        # Verificamos que los datos sean válidos. 
        if form.is_valid(): 
            # Guardamos el usuario.
            form.save() 
            # Después del registro enviamos al usuario a la página de login. 
            return redirect('login') 
    else: 
        # Si es una petición GET, creamos un formulario vacío. 
        form = RegistroUsuarioForm()
        
    # Mostramos el archivo HTML (se ejecuta para GET y para POST con errores). 
    return render( 
        request, 'usuarios/registro.html', 
        { 
            'form': form 
        } 
    )

@login_required
def editar_perfil(request):
    # Si recibimos información del formulario...
    if request.method == 'POST':
        form = EditarUsuarioForm(
            request.POST,
            instance=request.user
        )
        if form.is_valid():
            # Guardamos los cambios.
            form.save()
            # Regresamos a bienvenida.
            return redirect('bienvenida')
    else:
        # Cuando solamente abrimos la página (GET), cargamos los datos actuales.
        form = EditarUsuarioForm(
            instance=request.user
        )
        
    # Mostramos el archivo HTML para GET o para POST con errores.
    return render(
        request,
        'usuarios/editar_perfil.html',
        {
            'form': form
        }
    )

@login_required
def eliminar_cuenta(request):
    # Por seguridad solamente eliminamos si la petición utiliza POST.
    if request.method == 'POST':
    # Obtenemos al usuario autenticado.
        usuario = request.user
    # Eliminamos el registro.
        usuario.delete()
    # Volvemos al login.
        return redirect('login')
    # Si todavía no confirmó, mostramos una página de confirmación.
    return render(
    request,
    'usuarios/eliminar_cuenta.html'
    )
