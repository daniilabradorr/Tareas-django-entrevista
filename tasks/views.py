from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, DetailView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin # Para requerrir que el usuario este logueado para acceder a las vistas de tareas

#En este archivo realizo las vistas de las tareas, es decir, listado de tareas, crear tarea, editarla, eliminar y ver en detalle esa tarea.

#Clase de vista para listar todas las tareas
class TareaListView(ListView):
    model= Task
    template_name = 'task/task_list.html' #Template que se va a usar para mostrar la lista de tareas
    context_object_name = 'tareas' #Esto lo pongo para que en el template pueda acceder a las tareas con este nombre 
    paginate_by = 10 #Esto es para paginar las tareas

    #Unicamente un mensaje de error de que no tiene permiso para ver la lista de tareas
    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para ver esta página.')
        return super().handle_no_permission()

#Clase para crear una nueva tarea
class TareaCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm # Aqui unicamente lo que hago es decirle que formulario tiene que usar para crear la tarea (el que ya definimos en forms.oy)
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list') #redirijo a la lista de tareas una vez que ha creado el usuario correctamente 
    
    #Con esta funcion lo que hago es mostrar un mensaje de exito cuando se crea bien la tarea y separar en una funcion para apartar la logica de la vista
    def form_valid(self, form):
        messages.success(self.request, 'Tarea creada correctamente')
        return super().form_valid(form)
    

    #Para el error el mensaje
    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear la tarea. Revisa los datos.')
        return super().form_invalid(form)


#Clase para editar una tarea
class TareaUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'

    #Con esta funcion lo que hago es redirigir a la vista de detalle de la tarea una vez que se ha editado correctamente, lo hago en una funcion para separar la logica al tener que pasarle unos parametros
    def get_success_url(self):
        return reverse_lazy('task:task_detail', kwargs={'pk': self.object.pk})

    #Con esta funcion lo que hago es mostrar un mensaje de exito cuando se edita bien la tarea y separar en una funcion para apartar la logica de la vista
    def form_valid(self, form):
        messages.success(self.request, 'Tarea editada correctamente')
        return super().form_valid(form)
    

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar la tarea. Por favor corrige los errores.')
        return super().form_invalid(form)
    

#Clase para elminar una tarea
class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task:task_list')

    def post(self, request, *args, **kwargs):
        # inyectamos el mensaje justo antes de procesar el POST
        messages.success(self.request, 'Tarea eliminada correctamente.')
        return super().post(request, *args, **kwargs)
    

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para eliminar esta tarea.')
        return super().handle_no_permission()
    

#Clase para ver el detalle de una tarea  
class TareaDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = 'tarea'  

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permiso para ver este detalle.')
        return super().handle_no_permission()