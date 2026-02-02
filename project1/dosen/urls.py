from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_dosen, name='input_dosen'),
    path('update/<int:pk>/', views.dosen_update, name='dosen_update'),
    path('delete/<int:pk>/', views.dosen_delete, name='dosen_delete'),
    path('export/csv/', views.export_dosen_csv, name='export_dosen_csv'),
    path('export/excel/', views.export_dosen_excel, name='export_dosen_excel'),]