# En los PC de INACAP:
1. Instala Git, conectate a github
2. Presiona la tecla Windows y escribe Configuración (o ve a Settings).
3. Entra en Aplicaciones (Apps) > Configuración avanzada de aplicaciones > Alias de ejecución de aplicaciones (App execution aliases).
4. Busca en la lista los elementos relacionados con Python (python.exe y python3.exe).
5. Desactívalos (cambia el interruptor a Desactivado).
6. Habilitar codigo Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
7. Instalar en visual studio code:
- Python
- Dracula theme
- Indent rainbow
- Sql viewer
8. En el proyecto creado en visual:
- Hacer un .gitignore para el venv:
```
venv/
.venv/
env/
ENV/
```
9. En terminal:
```
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```
10. Crea y sigue las instrucciones del repositorio nuevo en github.(git init, branch, etc)

Recuerda:
```
git add . (prepara los cambios nuevos)
git commit -m "Describe lo que hiciste aquí" (guarda localmente)
git push (sube a GitHub)
```
Además:
```
git clone url del proyecto (para clonar proyectos)
```

# Instalación python, django, venv, configuración, models, migraciones y admin.

Crea entorno virtual:
```
python -m venv venv 
```
Activar el entorno en windows:
```
venv\Scripts\activate 
```
Activar entorno en Mac:
```
source venv/bin/activate
```
sale (venv) al principio si sale todo bien

Comprobar que este instalado:
```
django-admin --version 
```
Instalar Django:
```
pip install django
```