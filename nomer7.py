def revString(mystr):
    stack=[]
    penghitung = len(mystr)
    a = 1
    while a <= penghitung:
        b = a*(-1)
        stack.append(mystr[b])
        a=a+1
    cetak = ""
    for i in range(len(stack)):
        cetak += stack[i]
    return cetak

pembalikan = (input("Masukkan Kalimat "))
print("Kalimat setelah dibalik = ", revString(pembalikan))