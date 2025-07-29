from django.urls import path
from . import views  # Asegúrate de tener un archivo views.py

urlpatterns = [
    path('', views.producto_list, name='producto_list'),
    path('crear/', views.producto_create, name='producto_create'),
    path('<int:pk>/', views.producto_detail, name='producto_detail'),
    path('<int:pk>/editar/', views.producto_update, name='producto_update'),
    path('<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
]