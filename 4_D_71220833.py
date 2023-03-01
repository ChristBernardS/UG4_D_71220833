list_angka_input_disni = input('Masukkan sekumpulan bilangan (pisahkan dengan koma): ').split(',')
for i in range(len(list_angka_input_disni)):
    list_angka_input_disni[i] = int(list_angka_input_disni[i])
b = lambda x : max(list_angka_input_disni)
c = lambda x : min(list_angka_input_disni)
print(f"Bilangan terbesar dari kumpulan bilangan yang di input adalah {b(list_angka_input_disni)}")
print(f"Bilangan terkecil dari kumpulan bilangan yang di input adalah {c(list_angka_input_disni)}")