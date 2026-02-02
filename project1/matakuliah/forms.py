from django import forms
from .models import MataKuliah

class MataKuliahForm(forms.ModelForm):
    class Meta:
        model = MataKuliah
        fields = ['nama_mk', 'kode_mk', 'sks', 'semester', 'mhs_mk', 'dosen_mk']
        widgets = {
            'nama_mk': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan nama mata kuliah'
            }),
            'kode_mk': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan kode mata kuliah'
            }),
            'sks': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan SKS'
            }),
            'semester': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan semester'
            }),
            'mhs_mk': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
            'dosen_mk': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
        }
