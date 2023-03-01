# def nyari_panjang_kata(x):
#     x.split(' ')
#     i = 0
#     d = 0
#     while i < len(x):
#         b = x[i]
#         c = b.split()
#         i += 1
#         if c >= d:
#             d = c
#             e = i
#     return x[e]

a = input('Masukkan sebuah kalimat: ').split(' ')
# print(f"Kata terpanjang dalam kalimat tersebut adalah: {nyari_panjang_kata(a)}")

i = 0
d = 0
while i < len(a):
    b = a[i]
    c = b.split()
    i += 1
    if len(c) >= d:
        d = len(c)
        e = i