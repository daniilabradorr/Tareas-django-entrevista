from django.urls import path, include
from . import views

app_name = 'task'

urlpatterns = [
    path('',             views.TareaListView.as_view(),   name='task_list'),
    path('nueva/',       views.TareaCreateView.as_view(), name='task_create'),
    path('<int:pk>/',    views.TareaDetailView.as_view(), name='task_detail'),  
    path('editar/<int:pk>/', views.TareaUpdateView.as_view(), name='task_update'),
    path('eliminar/<int:pk>/', views.TareaDeleteView.as_view(), name='task_delete'),
]