def ganjil(bawah, atas):
    deret = []
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                deret.append(i)
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                deret.append(i)
    return deret

def main():
    x = [(10, 30), (97, 82)]

    for bawah, atas in x:
        hasil = ganjil(bawah, atas)

        if bawah < atas:
            print(f"Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah: {', '.join(map(str, hasil))}.")
        else:
            print(f"Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah: {', '.join(map(str, hasil))}.")

if __name__ == "__main__":
    main()
