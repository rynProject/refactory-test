jumlah= float()
besar = float ()
kecil = float ("inf")
nilai = int(input("Masukkan jumlah data: "))
print("Masukkan nilai data:")
for x in range(0, nilai):
    urut = float(input("nilai ke %d: " %(x+1)))
    if(urut > besar):
        besar = urut
    elif (urut < kecil):
        kecil = urut
    jumlah = jumlah + urut
    average = jumlah / nilai
print("jumlah nilai data: ", jumlah)
print("nilai rata-rata: ", average)
print ("nilai terbesar: ", besar)
print("nilai terkecil: ", kecil)