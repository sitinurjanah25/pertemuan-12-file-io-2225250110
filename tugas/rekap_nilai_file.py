
def baca_nilai(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, nilai = baris.split(",")
                    nilai = float(nilai)
                    data_nilai.append((nim, nilai))
                except ValueError:
                    print("Data tidak valid, dilewati:", baris)

    except FileNotFoundError:
        print("Error: File nilai tidak ditemukan.")

    return data_nilai


def buat_rekap(data_nilai):
    if not data_nilai:
        print("Tidak ada data nilai yang valid.")
        return

    jumlah = len(data_nilai)
    total = sum(nilai for nim, nilai in data_nilai)
    rata_rata = total / jumlah
    nilai_tertinggi = max(nilai for nim, nilai in data_nilai)
    nilai_terendah = min(nilai for nim, nilai in data_nilai)
    jumlah_lulus = sum(1 for nim, nilai in data_nilai if nilai >= 60)

    hasil = (
        "HASIL REKAP NILAI MAHASISWA\n"
        "===========================\n"
        f"Jumlah data valid: {jumlah}\n"
        f"Rata-rata nilai: {rata_rata:.2f}\n"
        f"Nilai tertinggi: {nilai_tertinggi:.2f}\n"
        f"Nilai terendah: {nilai_terendah:.2f}\n"
        f"Jumlah mahasiswa lulus: {jumlah_lulus}\n"
    )

    print(hasil)

    with open("data/hasil_rekap.txt", "w", encoding="utf-8") as file:
        file.write(hasil)

    print("Hasil rekap berhasil disimpan ke data/hasil_rekap.txt.")


def main():
    data_nilai = baca_nilai("data/nilai.txt")
    buat_rekap(data_nilai)


if __name__ == "__main__":
    main()
