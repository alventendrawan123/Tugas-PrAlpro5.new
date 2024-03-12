def perkalian(a, b):
    hasil = 0
    for i in range(b):
        hasil += a
    return hasil

def x(a, b):
    hasil = perkalian(a, b)
    P= " + ".join([str(a) for i in range(b)])
    print(f"{a} x {b} = {P} = {hasil}")

def main():
    tes_perkalian = [(5, 6), (10, 7)]

    for a1, a2 in tes_perkalian:
        x(a1, a2)

if __name__ == "__main__":
    main()
