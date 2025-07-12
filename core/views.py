from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm


from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


#En este archivo pongo las vistas core, es decir las generales (home, si tuviesemos pagina about, contacto, etc)

#Vista home / pagina de inicio
def home (request):
    return render(request, 'core/home.html')


#Clase customizada para el login (unciamente lo que cambio con el default der login es el mensaje de exito que le añado con SuccessMessageMixin)
class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = 'Has iniciado sesión correctamente.'
    redirect_authenticated_user = True  # si ya está logueado, redirige sin mostrar el formulario 


#Funcion para registrar un nuevo usuario cpon el def form_valid para verificar que el formulario se ha enviado correctamente y mostrar un mensaje de exito
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada correctamente. Ya puedes iniciar sesión.')
            return redirect('core:login')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})