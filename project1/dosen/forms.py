from django import forms
from .models import Dosen

class DosenForm(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = ['nama', 'nidn', 'email', 'no_hp', 'alamat', 'homebase']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan nama dosen'
            }),
            'nidn': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan NIDN'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan email'
            }),
            'no_hp': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': '08xx....'
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan alamat',
                'rows': 3
            }),
            'homebase': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan homebase/departemen'
            }),
        }
