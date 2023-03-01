def aritmatika(a, b, n):
    s = (n/2) * ((2*a) + ((n-1)*b) )
    return s

print(f"{20*'='} BARIS ARITMATIKA {20*'='}")
a = int(input('Masukkan bilangan awal : '))
b = int(input('Masukkan selisih bilangan : '))
c = int(input('Masukkan banyaknya suku : '))
print(f"Total dari deret aritmatika tersebut adalah : {aritmatika(a, b, c)}")