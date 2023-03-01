def aritmatika(a, b, n):
    s = (n/2) * ((2*a) + ((n-1)*b) )
    return s

print(f"{20*'='} BARIS ARITMATIKA {20*'='}")
angka_awal = int(input('Masukkan bilangan awal : '))
selisih_angka = int(input('Masukkan selisih bilangan : '))
total_suku = int(input('Masukkan banyaknya suku : '))
print(f"Total dari deret aritmatika tersebut adalah : {aritmatika(angka_awal, selisih_angka, total_suku)}")