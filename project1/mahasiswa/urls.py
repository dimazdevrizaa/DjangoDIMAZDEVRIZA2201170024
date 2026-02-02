from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_mahasiswa, name='input_mahasiswa'), 
    path('update/<int:pk>/', views.mahasiswa_update, name='mahasiswa_update'),
    path('delete/<int:pk>/', views.mahasiswa_delete, name='mahasiswa_delete'),
    path('export/csv/', views.export_mahasiswa_csv, name='export_mahasiswa_csv'),
    path('export/excel/', views.export_mahasiswa_excel, name='export_mahasiswa_excel'),
    path('export/all/csv/', views.export_all_data_csv, name='export_all_data_csv'),
    path('export/all/excel/', views.export_all_data_excel, name='export_all_data_excel'),
    path('api/dashboard-stats/', views.dashboard_stats, name='dashboard_stats'),
]

