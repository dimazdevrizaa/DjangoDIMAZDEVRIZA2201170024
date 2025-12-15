from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
    jurusan = forms.ChoiceField(
        choices=[('', 'Pilih Jurusan')] + list(Mahasiswa.JURUSAN_CHOICES),
        widget=forms.Select(attrs={
            'class': 'form-control form-control-sm',
        }),
        required=True,
        error_messages={
            'required': 'Jurusan harus dipilih',
        }
    )
    
    class Meta:
        model = Mahasiswa
        fields = ['nama', 'npm', 'email', 'no_hp', 'jurusan', 'alamat']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan nama'
            }),
            'npm': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Masukkan NPM'
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
        }