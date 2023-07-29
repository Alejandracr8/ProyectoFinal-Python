from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_cilindros, name='listar_cilindros'),
    path('crear/', views.crear_cilindro, name='crear_cilindro'),
    path('editar/<int:cilindro_id>/', views.editar_cilindro, name='editar_cilindro'),
    path('borrar/<int:cilindro_id>/', views.borrar_cilindro, name='borrar_cilindro'),
]

