from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


app_name = 'core' #Esto es para que en las urls de los tempplates a las vistas core les pueda poner el nameespace core y asi de esta manera, primero no haya conflictos con las urls de otras apps y segundo, para que no se repitan los nombres de las vistas en caso de que haya mas apps con vistas similares


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('core:home'), http_method_names=['post']), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]