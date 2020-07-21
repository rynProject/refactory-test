a = []
number = int(input("Masukkan nilai total element : "))
for i in range(number):
    value = int(input("Masukkan nilai %d element list : " %i))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("Hasil sorting ascending  : ", a)