x = input("Bir sayı gir: ")
print(x)
toplam = 0
for y in str(x):
    toplam = toplam + int(y)**int(len(x))

if(toplam == int(x)):
    print("Armstrong sayısı")    
else:
    print("değil")