tahun1 = int(input("Tahun 1 = "))
tahun2 = int(input("Tahun 2 = "))

def kabisat(n):
    if n%4==0:
        return True
    if n%400==0:
        return True
    if n%100==0:
        return True
    else:
        return False

for i in range(tahun1, tahun2):
    if kabisat(i):
        print(str(i)+" adalah tahun kabisat")

