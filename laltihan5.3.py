def hitung_ips(jumlah_matkul):
    total_sks = 0
    total_bobot_nilai = 0

    for i in range(1, jumlah_matkul + 1):
        nilai = input(f"Nilai MK {i}: ").upper()

        if nilai == "A":
            bobot = 4
        elif nilai == "B":
            bobot = 3
        elif nilai == "C":
            bobot = 2
        elif nilai == "D":
            bobot = 1
        else:
            print("Input tidak valid. Masukkan nilai A, B, C, atau D.")
            continue

        sks = 6
        total_sks += sks
        total_bobot_nilai += bobot * sks

    ips = total_bobot_nilai / total_sks
    return ips

def main():
    print("Program penghitung IPS Mahasiswa")
    jumlah_matkul = int(input("Berapa jumlah mata kuliah? "))
    ips = hitung_ips(jumlah_matkul)
    print(f"Nilai IPS anda semester ini {ips:.2f}")

if __name__ == "__main__":
    main()
