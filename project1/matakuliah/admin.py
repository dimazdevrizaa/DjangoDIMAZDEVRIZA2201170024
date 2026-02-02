from django.contrib import admin
from .models import MataKuliah

@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_mk', 'kode_mk', 'sks', 'semester', 'dosen_mk')
    search_fields = ('nama_mk', 'kode_mk')
    filter_horizontal = ('mhs_mk',)
