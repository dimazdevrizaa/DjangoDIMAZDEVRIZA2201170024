# Quick Start Guide - Export Feature

## 🎯 Lokasi Export Buttons

### Halaman Utama - Tampilkan Semua Data
**URL:** `http://localhost:8000/tampilkan-semua-data/`

```
┌─────────────────────────────────────────┐
│ DATA MAHASISWA                          │
├─────────────────────────────────────────┤
│ [Tabel Data Mahasiswa]                  │
├─────────────────────────────────────────┤
│ [CSV]  [Excel]                          │  ← Export Individual
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ DATA DOSEN                              │
├─────────────────────────────────────────┤
│ [Tabel Data Dosen]                      │
├─────────────────────────────────────────┤
│ [CSV]  [Excel]                          │  ← Export Individual
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ DATA MATA KULIAH                        │
├─────────────────────────────────────────┤
│ [Tabel Data Mata Kuliah]                │
├─────────────────────────────────────────┤
│ [CSV]  [Excel]                          │  ← Export Individual
└─────────────────────────────────────────┘

[Export Semua Data (CSV)]  [Export Semua Data (Excel)]  ← Export All
```

### Halaman Input Mahasiswa
**URL:** `http://localhost:8000/mahasiswa/input/`

```
┌─────────────────────────────────────────┐
│ FORM INPUT MAHASISWA                    │
├─────────────────────────────────────────┤

[Form fields...]

[Simpan]  [Kembali]

├─────────────────────────────────────────┤
│ DAFTAR MAHASISWA                        │
├─────────────────────────────────────────┤
│ [Tabel Data Mahasiswa]                  │
│ dengan search & filter                  │
├─────────────────────────────────────────┤
│ [CSV Export]  [Excel Export]            │  ← Export dengan filter aktif
└─────────────────────────────────────────┘
```

### Halaman Input Dosen
**URL:** `http://localhost:8000/dosen/input/`

```
┌─────────────────────────────────────────┐
│ FORM INPUT DOSEN                        │
├─────────────────────────────────────────┤

[Form fields...]

[Simpan]  [Kembali]

├─────────────────────────────────────────┤
│ DAFTAR DOSEN                            │
├─────────────────────────────────────────┤
│ [Tabel Data Dosen]                      │
│ dengan search                           │
├─────────────────────────────────────────┤
│ [CSV Export]  [Excel Export]            │  ← Export dengan filter aktif
└─────────────────────────────────────────┘
```

### Halaman Input Mata Kuliah
**URL:** `http://localhost:8000/matakuliah/input/`

```
┌─────────────────────────────────────────┐
│ FORM INPUT MATA KULIAH                  │
├─────────────────────────────────────────┤

[Form fields...]

[Simpan]  [Kembali]

├─────────────────────────────────────────┤
│ DAFTAR MATA KULIAH                      │
├─────────────────────────────────────────┤
│ [Tabel Data Mata Kuliah]                │
│ dengan search                           │
├─────────────────────────────────────────┤
│ [CSV Export]  [Excel Export]            │  ← Export dengan filter aktif
└─────────────────────────────────────────┘
```

---

## 📥 Format File yang Dihasilkan

### CSV Format
```
📄 mahasiswa_20260120_143025.csv
📄 dosen_20260120_143025.csv
📄 matakuliah_20260120_143025.csv
📄 semua_data_20260120_143025.csv
```
- Format text biasa
- Dibuka dengan Excel, Google Sheets, etc
- Separator: comma (,)

### Excel Format
```
📊 mahasiswa_20260120_143025.xlsx
📊 dosen_20260120_143025.xlsx
📊 matakuliah_20260120_143025.xlsx
📊 semua_data_20260120_143025.xlsx (3 sheets)
```
- Format binary profesional
- Header dengan warna styling
- Column width otomatis
- Multiple sheets untuk semua data

---

## ⚙️ Technical Details

### Routes (URLs)

**Mahasiswa:**
- `GET /mahasiswa/export/csv/` → Export mahasiswa CSV
- `GET /mahasiswa/export/excel/` → Export mahasiswa Excel
- `GET /mahasiswa/export/all/csv/` → Export semua data CSV
- `GET /mahasiswa/export/all/excel/` → Export semua data Excel

**Dosen:**
- `GET /dosen/export/csv/` → Export dosen CSV
- `GET /dosen/export/excel/` → Export dosen Excel

**Mata Kuliah:**
- `GET /matakuliah/export/csv/` → Export mata kuliah CSV
- `GET /matakuliah/export/excel/` → Export mata kuliah Excel

### Query Parameters

Semua endpoint mendukung query parameters untuk mempertahankan filter saat export:

```
/mahasiswa/export/csv/?q=Ahmad&jurusan=Teknologi Informasi
/dosen/export/csv/?q=Dr
/matakuliah/export/csv/?q=Algoritma
```

### Security
- ✓ Semua endpoint dilindungi `@login_required`
- ✓ Hanya authenticated users yang bisa download
- ✓ No SQL injection risks (menggunakan Django ORM)

---

## 🚀 Cara Menggunakan

### Step 1: Login
Login ke aplikasi Django admin interface atau user account

### Step 2: Navigasi ke Halaman dengan Tabel
Pilih salah satu:
- Tampilkan Semua Data
- Input Mahasiswa
- Input Dosen
- Input Mata Kuliah

### Step 3: (Optional) Filter Data
Jika halaman memiliki filter:
- Gunakan search box
- Gunakan kategori/dropdown
- Klik "Filter" atau "Cari"

### Step 4: Export
Scroll ke bawah tabel dan klik:
- `[CSV Export]` untuk format CSV
- `[Excel Export]` untuk format Excel

### Step 5: Download Selesai
File akan otomatis diunduh ke folder Downloads

---

## 💾 Kolom yang Di-Export

### Mahasiswa
| No | Nama | NPM | Email | No. HP | Jurusan | Alamat |

### Dosen
| No | Nama | NIDN | Email | No. HP | Homebase | Alamat |

### Mata Kuliah
| No | Nama MK | Kode MK | SKS | Semester | Dosen | Jumlah Mahasiswa |

---

## 🎨 Excel Header Colors

| Tabel | Warna | Hex Code |
|-------|-------|----------|
| Mahasiswa | 🔵 Biru | #667eea |
| Dosen | 🟢 Hijau | #28a745 |
| Mata Kuliah | 🟡 Kuning | #ffc107 |

---

## 📋 Checklist

- ✅ Export CSV untuk Mahasiswa
- ✅ Export CSV untuk Dosen
- ✅ Export CSV untuk Mata Kuliah
- ✅ Export Excel untuk Mahasiswa
- ✅ Export Excel untuk Dosen
- ✅ Export Excel untuk Mata Kuliah
- ✅ Export Semua Data (CSV + Excel)
- ✅ Support Filter Parameters
- ✅ Security dengan @login_required
- ✅ Beautiful UI dengan Bootstrap Icons
- ✅ Timestamp Automatic Naming
- ✅ openpyxl Package Installed

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Export button tidak muncul | Clear cache browser (Ctrl+Shift+Del) |
| Excel export error | Pastikan `pip install openpyxl` sudah dijalankan |
| File tidak download | Check popup blocker di browser |
| Filter tidak tersimpan saat export | Gunakan URL dengan query parameters |
| CSV tidak bisa dibuka | Gunakan UTF-8 encoding di Excel |

---

## 📚 Dokumentasi Lengkap

Untuk informasi lebih detail, lihat:
- `EXPORT_FEATURE.md` - Dokumentasi lengkap fitur
- `IMPLEMENTATION_SUMMARY.md` - Summary implementasi teknis

---

**Status: ✅ SELESAI DAN SIAP DIGUNAKAN**

Semua fitur export telah diimplementasikan dan tested. Anda bisa langsung menggunakannya!
