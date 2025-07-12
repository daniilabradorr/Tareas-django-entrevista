from django import forms
from .models import Task

#He creado este arcivho para separar mejor la lógica y en el solo tener el formulario de las tareas(TaskForm)
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description'] #Aqui establezco los campos que quiero que aparezcan en el formulario
        
        #Los widgets son para darle un estilo al formulario, en este caso le doy un estilo de bootstrap
        #Si no lo pongo, el formulario se veria muy feo y sin estilo, pero que le puedes tu luego darle el estilo que quieras a mano
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la tarea'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': 'Descripcion de la tarea'}),
        }

        # Esta funcion que he puesto es para validar el titulo de la tarea, y tambien para que tenga mas de 3 caracteres de longitud
        def clean_title(self):
            title = self.cleaned_data.get('title')
            if Task.objects.filter(title=title).exists():
                raise forms.ValidationError("Ya existe una tarea con este titulo")
            if len(title) < 3:
                raise forms.ValidationError('El título debe tener al menos 3 caracteres.')
            return title