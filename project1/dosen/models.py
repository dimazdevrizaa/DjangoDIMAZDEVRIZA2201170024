from django.db import models

class Dosen(models.Model):
    nama = models.CharField(max_length=100)
    nidn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    no_hp = models.CharField(max_length=20, blank=True)
    alamat = models.TextField(blank=True)
    homebase = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nama} ({self.nidn})"
