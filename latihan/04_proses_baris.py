
with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if baris:
            nim, nilai = baris.split(",")
            print("NIM:", nim)
            print("Nilai:", float(nilai))
