# project1/mahasiswa/models.py
from django.db import models

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
