hasil = 0

while True:
    line = input("Masukkan Angka untuk dihitung ")
    try:
        hasil+=int(line)
    except ValueError:
        break
print(hasil)