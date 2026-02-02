"""
Test suite untuk form validation dan data standardization
Mendemonstrasikan implementasi clean() method
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Mahasiswa
from .forms import MahasiswaForm


class MahasiswaFormValidationTests(TestCase):
    """Test validasi dan standarisasi data di Form level"""
    
    def test_nama_standardization_to_title_case(self):
        """Test: Nama di-standardisasi ke title case"""
        form_data = {
            'nama': 'budi santoso',  # input lowercase
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '081234567890',
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        # Check if nama is standardized to title case
        self.assertEqual(form.cleaned_data['nama'], 'Budi Santoso')
    
    def test_nama_with_extra_whitespace(self):
        """Test: Nama dengan whitespace extra di-clean"""
        form_data = {
            'nama': 'budi    santoso   ',  # multiple spaces
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '081234567890',
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        # Check if extra spaces removed
        self.assertEqual(form.cleaned_data['nama'], 'Budi Santoso')
    
    def test_nama_minimal_length(self):
        """Test: Nama kurang dari 3 karakter di-reject"""
        form_data = {
            'nama': 'AB',  # kurang dari 3 karakter
            'npm': '2023001',
            'email': 'ab@example.com',
            'no_hp': '081234567890',
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nama', form.errors)
    
    def test_npm_validation_harus_angka(self):
        """Test: NPM hanya boleh berisi angka"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '202300A',  # ada huruf
            'email': 'budi@example.com',
            'no_hp': '081234567890',
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('npm', form.errors)
    
    def test_npm_minimal_length(self):
        """Test: NPM minimal 5 digit"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023',  # kurang dari 5 digit
            'email': 'budi@example.com',
            'no_hp': '081234567890',
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('npm', form.errors)
    
    def test_npm_uniqueness(self):
        """Test: NPM harus unique"""
        # Create first mahasiswa
        Mahasiswa.objects.create(
            nama='Budi Santoso',
            npm='2023001',
            email='budi@example.com',
            jurusan='Teknologi Informasi'
        )
        
        # Try create dengan npm yang sama
        form_data = {
            'nama': 'Siti Nurhaliza',
            'npm': '2023001',  # NPM yang sama
            'email': 'siti@example.com',
            'no_hp': '082345678901',
            'jurusan': 'Sains Data',
            'alamat': 'Jl. Ahmad Yani No. 5'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('npm', form.errors)
        self.assertIn('sudah terdaftar', str(form.errors))
    
    def test_email_standardization_lowercase(self):
        """Test: Email di-standardisasi ke lowercase"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023001',
            'email': 'BUDI@EXAMPLE.COM',  # uppercase
            'no_hp': '081234567890',
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        # Check if email is lowercase
        self.assertEqual(form.cleaned_data['email'], 'budi@example.com')
    
    def test_email_uniqueness(self):
        """Test: Email harus unique"""
        # Create first mahasiswa
        Mahasiswa.objects.create(
            nama='Budi Santoso',
            npm='2023001',
            email='budi@example.com',
            jurusan='Teknologi Informasi'
        )
        
        # Try create dengan email yang sama
        form_data = {
            'nama': 'Siti Nurhaliza',
            'npm': '2023002',
            'email': 'budi@example.com',  # email yang sama
            'no_hp': '082345678901',
            'jurusan': 'Sains Data',
            'alamat': 'Jl. Ahmad Yani No. 5'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    def test_no_hp_validation_format(self):
        """Test: No HP harus format Indonesia (08xx atau 628xx)"""
        # Test dengan format tidak valid
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '123456789',  # format tidak valid
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('no_hp', form.errors)
    
    def test_no_hp_valid_format_08(self):
        """Test: No HP dengan format 08xx adalah valid"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '081234567890',  # format valid
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
    
    def test_no_hp_valid_format_628(self):
        """Test: No HP dengan format 628xx adalah valid"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '628123456789',  # format valid
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
    
    def test_no_hp_cleanup_spaces_and_dashes(self):
        """Test: No HP dengan spaces/dashes di-clean"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '08-1234-567-890',  # dengan dashes
            'jurusan': 'Teknologi Informasi',
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        # Check if dashes removed
        self.assertEqual(form.cleaned_data['no_hp'], '081234567890')
    
    def test_jurusan_must_be_selected(self):
        """Test: Jurusan harus dipilih (tidak boleh kosong)"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '081234567890',
            'jurusan': '',  # empty
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('jurusan', form.errors)
    
    def test_jurusan_must_valid_choice(self):
        """Test: Jurusan harus dari list yang valid"""
        form_data = {
            'nama': 'Budi Santoso',
            'npm': '2023001',
            'email': 'budi@example.com',
            'no_hp': '081234567890',
            'jurusan': 'Invalid Jurusan',  # tidak ada di choices
            'alamat': 'Jl. Merdeka No. 1'
        }
        form = MahasiswaForm(data=form_data)
        # Form akan reject karena tidak ada di choices
        self.assertFalse(form.is_valid())
        self.assertIn('jurusan', form.errors)


class MahasiswaModelValidationTests(TestCase):
    """Test validasi di Model level"""
    
    def test_model_nama_standardization(self):
        """Test: Model juga standardisasi nama ke title case"""
        m = Mahasiswa(
            nama='budi santoso',
            npm='2023001',
            email='budi@example.com',
            jurusan='Teknologi Informasi'
        )
        m.clean()  # Run validation
        self.assertEqual(m.nama, 'Budi Santoso')
    
    def test_model_email_standardization(self):
        """Test: Model standardisasi email ke lowercase"""
        m = Mahasiswa(
            nama='Budi Santoso',
            npm='2023001',
            email='BUDI@EXAMPLE.COM',
            jurusan='Teknologi Informasi'
        )
        m.clean()  # Run validation
        self.assertEqual(m.email, 'budi@example.com')
    
    def test_model_npm_validation(self):
        """Test: Model validasi NPM harus angka"""
        m = Mahasiswa(
            nama='Budi Santoso',
            npm='202300A',  # invalid
            email='budi@example.com',
            jurusan='Teknologi Informasi'
        )
        with self.assertRaises(ValidationError):
            m.clean()
    
    def test_model_no_hp_format_validation(self):
        """Test: Model validasi format no HP"""
        m = Mahasiswa(
            nama='Budi Santoso',
            npm='2023001',
            email='budi@example.com',
            no_hp='123456789',  # invalid format
            jurusan='Teknologi Informasi'
        )
        with self.assertRaises(ValidationError):
            m.clean()


class DataStandardizationIntegrationTests(TestCase):
    """Integration test: dari form submit hingga database"""
    
    def test_complete_flow_dengan_lowercase_input(self):
        """Test: Data dengan lowercase input ter-standardisasi dengan benar"""
        form_data = {
            'nama': 'budi santoso sering',  # input lowercase
            'npm': '2023001',
            'email': 'BUDI@EXAMPLE.COM',  # uppercase
            'no_hp': '08-1234-567-890',  # dengan dashes
            'jurusan': 'Teknologi Informasi',
            'alamat': 'jl. merdeka no. 1'  # lowercase
        }
        
        form = MahasiswaForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        
        # Save dan check database
        instance = form.save(commit=False)
        instance.full_clean()
        instance.save()
        
        # Query dari database
        saved = Mahasiswa.objects.get(npm='2023001')
        
        # Verify standardization
        self.assertEqual(saved.nama, 'Budi Santoso Sering')  # title case
        self.assertEqual(saved.email, 'budi@example.com')  # lowercase
        self.assertEqual(saved.no_hp, '081234567890')  # dashes removed
    
    def test_validation_error_messages_are_clear(self):
        """Test: Error messages user-friendly dan jelas"""
        form_data = {
            'nama': 'AB',  # too short
            'npm': '202300A',  # invalid format
            'email': 'budi@invalid',  # invalid email
            'no_hp': '12345',  # invalid format
            'jurusan': '',  # empty
            'alamat': 'Jl. Merdeka'
        }
        form = MahasiswaForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        # Check error messages are informative
        errors_str = str(form.errors)
        self.assertTrue(len(errors_str) > 0)


# Run tests dengan: python manage.py test mahasiswa.tests
