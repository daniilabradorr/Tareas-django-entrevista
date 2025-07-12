from django.db import models

#AQUI realizo la declaracion del modelo de task, tarea

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Titulo') #El verbose_name es para que en el admin de django se muestre el nombre que yo quiera. asi en lugar de mostratelo en ingles de lo muestra en español
    description = models.TextField(blank=True, verbose_name = 'Descripcion') #El blank=True es para que el campo no sea obligatorio, asi puede solo tener titulo y no descripcion
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    
    # La clase Meta la uso para definir opciones adicionales del modelo 
    class Meta:
        db_table = 'tasks' #Nombre de la tabla de la base de datos
        ordering = ['-created_at'] #Ordeno las tareas por fecha de creacion, de manera que salen de mas reciente a mas antigua
        managed = True #Esto es para que django maneje la tabla, es decir, que cree las migraciones y las tablas en la base de datos
        verbose_name = 'Tarea' #El verbose name tanto el singular como el plural es para que el admin de django lo muestre como yo quiera
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.title #Esto es la funcion de mostar el titulo de la tarea en lugar de el objeto en si, que es lo que hace por defecto django (funcion de toda la vida de python)