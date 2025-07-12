# Mis Tareas – Proyecto Django (Entrevista Técnica)

Aplicación *mobile-first* que demuestra un CRUD completo de tareas usando **Django 5**, **Bootstrap 5** y vistas basadas en clases (CBV).
La apliación es muy simple, sigue las reglas y lo establecido por lo pedido ya sea muy simple o complicado.
Los estilos estan realizados como ya he mencionado previamente en BootsTrap 5 ya que no pedia estilos para darle a ver a la persona encargada de la entrevista que se usa BootsTrap.

## ✨ Características

| Función | Detalle |
|---------|---------|
| CRUD completo | Crear, listar, editar y eliminar tareas |
| Autenticación | Login, logout, registro de usuario |
| Validaciones | Reglas en `forms.py` y mensajes flash (éxito / error) |
| UI responsiva | Bootstrap 5 + utilidades mobile-first |
| Seguridad | CSRF, logout por `POST`, mixins de acceso |
| Organización clara | Apps `core` (home / auth) y `task` (modelo + vistas) |


## 🏗️ Estructura

```text
MisTareas/
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── registration/
│           ├── login.html
│           └── register.html
├── task/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── task/
│           ├── base.html
│           ├── task_list.html
│           ├── task_form.html
│           ├── task_detail.html
│           └── task_confirm_delete.html
├── templates/               # plantillas globales (opcional)
│   └── registration/
│       └── logout.html
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

## 🚀 Instalación rápida


# Clonar repositorio
git clone https://github.com/daniilabradorr/Tareas-django-entrevista.git
cd Tareas-django-entrevista

# Crear y activar entorno virtual
python -m venv venv

# Linux/macOS: source venv/bin/activate
# Windows PowerShell:
(Dependiendo que sistema operativo tengan ustedes)
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# (o) instalar manualmente:
pip install django>=5.0,<6 bootstrap5

# Migraciones y superusuario
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
Visita http://127.0.0.1:8000/ para ver la aplicación.

📝 Uso
Regístrate o inicia sesión.

En la barra superior, pulsa “Nueva Tarea”.

Cumplimenta título (mín. 3 caracteres) y descripción.

Guarda; verás un mensaje verde de éxito.

Prueba a editar o eliminar; cada acción muestra su correspondiente alerta.

⚙️ Modelo
El modelo es sencillo pero me rijo unica y exclusivamente al enunciado

class Task(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
📂 Vistas clave
Vista	Clase	URL	Descripción

TareaListView - ListView - /tareas/ - Listado paginado
TareaCreateView - CreateView - /tareas/nueva/ - Valida y crea
TareaUpdateView - UpdateView - /tareas/editar/<pk>/ - Edita instancia
TareaDeleteView - DeleteView - /tareas/eliminar/<pk>/ - Confirma y borra
TareaDetailView - DetailView - /tareas/<pk>/ - Vista detalle

Las requeridas heredan LoginRequiredMixin; los mensajes flash se gestionan con messages.success() y messages.error().

🔒 Seguridad
CSRF en todos los formularios ({% csrf_token %}).

LogoutView restringido a POST para evitar CSRF por GET.

Validaciones del lado servidor en forms.py.


# 👩‍💻 Autor
Daniel Labrador Benito

# LinkedIn · GitHub
LinkedIn: https://www.linkedin.com/in/daniel-labrador-benito-6b794727b/
GitHub : https://github.com/daniilabradorr