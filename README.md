# Pertemuan 12 — File Input-Output dan Penanganan Error Dasar

## Identitas
- Nama: Siti Nurjanah
- NIM: 2225250110
- Kelas: 3E
- Program Studi: Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman

## Deskripsi
Tugas ini membahas penggunaan file input-output dalam Python serta penanganan error dasar. Program mempraktikkan cara menulis, membaca, dan menambahkan isi file, memproses data dari file, serta menangani `FileNotFoundError` dan `ValueError`.

## Struktur Folder
```text
pertemuan-12-file-io-2225250110/
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
├── tugas/
│   └── rekap_nilai_file.py
├── .gitignore
└── README.md
```

## Cara Menjalankan
Jalankan perintah berikut dari terminal di folder utama proyek:

```powershell
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
python tugas/rekap_nilai_file.py
```

## Format Data
File `data/nilai.txt` menggunakan format NIM dan nilai yang dipisahkan dengan koma.

Contoh:
```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Data dengan nilai yang tidak dapat dikonversi menjadi angka akan dilewati oleh program.

## Hasil Pengujian
- Jumlah data valid: 5
- Rata-rata nilai: 83.40
- Nilai tertinggi: 92.00
- Nilai terendah: 74.00
- Jumlah mahasiswa lulus: 5
- Data tidak valid berhasil dilewati.
- Hasil rekap disimpan ke `data/hasil_rekap.txt`.

## Refleksi
Melalui tugas ini, saya mempelajari cara mengolah file teks menggunakan Python, membaca data per baris, menambahkan isi file, serta menangani kesalahan saat file tidak ditemukan atau input tidak sesuai. Saya juga mempelajari penggunaan fungsi untuk memisahkan proses pembacaan dan pengolahan data.