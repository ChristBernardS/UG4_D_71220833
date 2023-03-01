def nyari_panjang_kata(x):
    i = 0
    d = 0
    while i < len(x):
        b = x[i]
        c = list(b)
        i += 1
        if len(c) >= d:
            d = len(c)
            e = i
    return x[e-1]

kalimat_input_disini = input('Masukkan sebuah kalimat: ').split(' ')
print(f"Kata terpanjang dalam kalimat tersebut adalah: {nyari_panjang_kata(kalimat_input_disini)}")