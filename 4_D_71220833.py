a = input('Masukkan sekumpulan bilangan (pisahkan dengan koma): ').split(', ')
for i in range(len(a)):
    a[i] = int(a[i])
b = lambda x : max(a)
c = lambda x : min(a)
print(f"Bilangan terbesar dari kumpulan bilangan yang di input adalah {b(a)}")
print(f"Bilangan terkecil dari kumpulan bilangan yang di input adalah {c(a)}")