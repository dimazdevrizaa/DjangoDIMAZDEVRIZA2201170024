from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_mahasiswa, name='input_mahasiswa'), 
    path('mahasiswa/update/<int:pk>/', views.mahasiswa_update, name='mahasiswa_update'),
    path('mahasiswa/delete/<int:pk>/', views.mahasiswa_delete, name='mahasiswa_delete'),
]