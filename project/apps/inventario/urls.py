from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_cilindros, name='list_cilindros'),
    path('create/', views.create_cilindro, name='create_cilindro'),
    path('edit/<int:cilindro_id>/', views.edit_cilindro, name='edit_cilindro'),
    path('delete/<int:cilindro_id>/', views.delete_cilindro, name='delete_cilindro'),
]

