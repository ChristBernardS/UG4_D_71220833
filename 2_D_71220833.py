angka = int(input('Masukkan sebuah angka: '))
def kuadrat(x):
    return lambda x : x**2
print(f"Hasil kuadrat dari angka {angka} adalah: {kuadrat(0)(angka)}")