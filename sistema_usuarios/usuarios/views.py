from django.shortcuts import render

# Create your views here.
# render permite cargar un archivo HTML.
# redirect permite enviar al usuario 
# hacia otra página. 
from django.shortcuts import render, redirect 
# Importamos nuestro formulario. 
from .forms import RegistroUsuarioForm
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
    # Comprobamos si el navegador está 
    # # enviando información mediante POST. 
    if request.method == 'POST': 
        # Creamos un formulario utilizando 
        # # la información recibida. 
        form = RegistroUsuarioForm( request.POST ) 
        # Verificamos que los datos sean válidos. 
        if form.is_valid(): 
            # Guardamos el usuario.
            # Django se encargará de almacenarlo 
            # en la base de datos. 
            form.save() 
            # Después del registro enviamos 
            # al usuario a la página de login. 
            return redirect('login') 
        else: 
            # Si solamente estamos entrando 
            # # a la página, creamos un formulario vacío. 
            form = RegistroUsuarioForm()
        # Mostramos el archivo HTML. 
        return render( 
            request, 'usuarios/registro.html', 
            { 
                'form': form 
                } 
            )