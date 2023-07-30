from django.urls import path
from . import views

app_name = "inventario"

urlpatterns = [path("", views.index, name="home")]


urlpatterns = [
    path('listar/', views.listar_cilindros.as_view, name='listar_cilindros'),
    path('crear/', views.crear_cilindro.as_view, name='crear_cilindro'),
    path('editar/<int:pk>/', views.editar_cilindro.as_view, name='editar_cilindro'),
    path('borrar/<int:pk>/', views.borrar_cilindro.as_view, name='borrar_cilindro'),
]

urlpatterns += [
    path("ubicacion/listar/", views.listar_ubicacion.as_view(), name="producto_list"),
    path("ubicacion/crear/", views.crear_ubicacion.as_view(), name="producto_create"),
    path("ubicacion/editar/<int:pk>", views.editar_ubicacion.as_view(), name="producto_update"),
    path("ubicacion/borrar/<int:pk>", views.borrar_ubicacion.as_view(), name="producto_delete"),
]