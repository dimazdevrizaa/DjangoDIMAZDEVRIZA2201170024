from django.contrib import admin
from .models import Dosen

@admin.register(Dosen)
class DosenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'nidn', 'email', 'no_hp', 'alamat', 'homebase')
    search_fields = ('nama', 'nidn', 'email')
