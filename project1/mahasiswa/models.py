# project1/mahasiswa/models.py
from django.db import models
from django.core.exceptions import ValidationError
import re

class Mahasiswa(models.Model):
    JURUSAN_CHOICES = [
        ('Teknologi Informasi', 'Teknologi Informasi'),
        ('Sains Data', 'Sains Data'),
    ]
    
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=20)
    email = models.EmailField()
    no_hp = models.CharField(max_length=20, blank=True)
    jurusan = models.CharField(max_length=100, choices=JURUSAN_CHOICES, blank=True)
    alamat = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nama} ({self.npm})"
    
    def clean(self):
        """
        Model-level validation dan standardisasi data
        Dijalankan sebelum save() untuk memastikan konsistensi data
        """
        # Standardisasi nama: title case
        if self.nama:
            self.nama = self.nama.title()
        
        # Standardisasi email: lowercase
        if self.email:
            self.email = self.email.lower().strip()
        
        # Standardisasi no_hp: hapus karakter non-digit kecuali awal
        if self.no_hp:
            self.no_hp = re.sub(r'[\s\-\+\(\)]+', '', self.no_hp)
        
        # Standardisasi alamat: capitalize first letter
        if self.alamat:
            self.alamat = ' '.join(self.alamat.split())
        
        # Validasi field
        errors = {}
        
        # Validasi NPM
        if self.npm:
            if not self.npm.isdigit():
                errors['npm'] = 'NPM harus berupa angka'
            elif len(self.npm) < 5:
                errors['npm'] = 'NPM minimal 5 digit'
        
        # Validasi no_hp format Indonesia
        if self.no_hp:
            if not (self.no_hp.startswith('08') or self.no_hp.startswith('628')):
                errors['no_hp'] = 'Format no HP harus 08xx atau 628xx'
        
        # Validasi jurusan dari choices yang tersedia
        if self.jurusan:
            valid_jurusans = [choice[0] for choice in self.JURUSAN_CHOICES]
            if self.jurusan not in valid_jurusans:
                errors['jurusan'] = f'Jurusan "{self.jurusan}" tidak valid'
        
        if errors:
            raise ValidationError(errors)