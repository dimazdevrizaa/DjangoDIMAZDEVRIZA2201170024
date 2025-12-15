from django.contrib import admin

# Register your models here.
from .models import Mahasiswa

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'npm', 'email', 'jurusan', 'no_hp')
    search_fields = ('nama', 'npm', 'email', 'jurusan')
