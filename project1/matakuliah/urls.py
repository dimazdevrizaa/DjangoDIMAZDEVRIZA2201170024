from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_matakuliah, name='input_matakuliah'),
    path('update/<int:pk>/', views.matakuliah_update, name='matakuliah_update'),
    path('delete/<int:pk>/', views.matakuliah_delete, name='matakuliah_delete'),
    path('export/csv/', views.export_matakuliah_csv, name='export_matakuliah_csv'),
    path('export/excel/', views.export_matakuliah_excel, name='export_matakuliah_excel'),]