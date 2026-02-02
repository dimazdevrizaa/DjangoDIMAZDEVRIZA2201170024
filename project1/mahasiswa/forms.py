from django import forms
from django.core.exceptions import ValidationError
import re
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
    
    def clean_nama(self):
        """
        Standardisasi nama: capitalize each word (title case)
        Contoh: "budi santoso" → "Budi Santoso"
        """
        nama = self.cleaned_data.get('nama')
        
        if nama:
            # Remove extra whitespace
            nama = ' '.join(nama.split())
            
            # Validate minimum length
            if len(nama) < 3:
                raise ValidationError('Nama minimal 3 karakter')
            
            # Standardize ke title case (capitalize each word)
            nama = nama.title()
        
        return nama
    
    def clean_npm(self):
        """
        Validasi NPM format: harus angka, minimal 5 digit
        Contoh format: 2023001
        """
        npm = self.cleaned_data.get('npm')
        
        if npm:
            # Remove whitespace
            npm = npm.strip()
            
            # Validate format: hanya angka
            if not npm.isdigit():
                raise ValidationError('NPM harus berupa angka saja (tidak boleh ada huruf atau simbol)')
            
            # Validate length
            if len(npm) < 5:
                raise ValidationError('NPM minimal 5 digit')
            
            if len(npm) > 20:
                raise ValidationError('NPM maksimal 20 digit')
            
            # Check NPM uniqueness (exclude current object if editing)
            qs = Mahasiswa.objects.filter(npm=npm)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            
            if qs.exists():
                raise ValidationError(f'NPM {npm} sudah terdaftar di sistem')
        
        return npm
    
    def clean_email(self):
        """
        Standardisasi email: convert ke lowercase
        Validasi email uniqueness
        """
        email = self.cleaned_data.get('email')
        
        if email:
            # Standardize ke lowercase
            email = email.lower().strip()
            
            # Check email uniqueness (exclude current object if editing)
            qs = Mahasiswa.objects.filter(email=email)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            
            if qs.exists():
                raise ValidationError(f'Email {email} sudah terdaftar di sistem')
        
        return email
    
    def clean_no_hp(self):
        """
        Standardisasi no HP: format Indonesia (08xx atau 628xx)
        Hapus karakter non-digit
        """
        no_hp = self.cleaned_data.get('no_hp')
        
        if no_hp:
            # Remove spaces and dashes
            no_hp = re.sub(r'[\s\-\+\(\)]+', '', no_hp)
            
            # Validate: hanya digit
            if not no_hp.isdigit():
                raise ValidationError('Nomor HP hanya boleh berisi angka')
            
            # Validate Indonesia format: 08xx atau 628xx
            if not (no_hp.startswith('08') or no_hp.startswith('628')):
                raise ValidationError('Nomor HP harus format Indonesia (08xx atau 628xx)')
            
            # Validate length
            if len(no_hp) < 10:
                raise ValidationError('Nomor HP terlalu pendek')
            
            if len(no_hp) > 15:
                raise ValidationError('Nomor HP terlalu panjang')
        
        return no_hp
    
    def clean_alamat(self):
        """
        Standardisasi alamat: capitalize each word, remove extra whitespace
        """
        alamat = self.cleaned_data.get('alamat')
        
        if alamat:
            # Remove extra whitespace
            alamat = ' '.join(alamat.split())
            
            # Optional: capitalize first letter of each word
            # alamat = alamat.title()
        
        return alamat
    
    def clean(self):
        """
        Form-level validation: validasi kombinasi field
        """
        cleaned_data = super().clean()
        
        nama = cleaned_data.get('nama')
        npm = cleaned_data.get('npm')
        jurusan = cleaned_data.get('jurusan')
        
        # Validasi kombinasi: jika ada nama dan npm, keduanya harus valid
        if nama and npm:
            # Contoh: validasi bahwa nama tidak hanya berisi angka
            if nama.replace(' ', '').isdigit():
                raise ValidationError('Nama tidak boleh hanya berisi angka')
        
        # Validasi: jurusan harus dipilih
        if not jurusan or jurusan == '':
            raise ValidationError({'jurusan': 'Jurusan harus dipilih'})
        
        # Validasi category: jurusan harus dari list yang valid
        valid_jurusans = [choice[0] for choice in Mahasiswa.JURUSAN_CHOICES]
        if jurusan not in valid_jurusans:
            raise ValidationError({'jurusan': f'Jurusan {jurusan} tidak valid'})
        
        return cleaned_data