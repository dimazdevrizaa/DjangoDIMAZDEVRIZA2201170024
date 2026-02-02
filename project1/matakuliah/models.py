from django.db import models
from mahasiswa.models import Mahasiswa
from dosen.models import Dosen

class MataKuliah(models.Model):
    nama_mk = models.CharField(max_length=100)
    kode_mk = models.CharField(max_length=20, unique=True)
    sks = models.IntegerField()
    semester = models.IntegerField()
    mhs_mk = models.ManyToManyField(Mahasiswa, related_name='matakuliah_set', blank=True)
    dosen_mk = models.ForeignKey(Dosen, on_delete=models.PROTECT, related_name='matakuliah_set')

    def __str__(self):
        return f"{self.nama_mk} ({self.kode_mk})"
