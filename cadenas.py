x=str(input("Dame una cadena: "))
print(x[0:2])
print(x[-3:])
for conso in x:
    if conso in 'bcdfghjklmnñpqrstvxzw':
        print(conso, end='')
    elif conso in 'QWRTYPSDFGHJKLÑZXCVBNM':
        print(conso, end='')
print("\n")


y=int(input("Dame una cadena de numeros: "))
print(y)
print("{:,}".format(y).replace(',','~').replace('.',',').replace('~','.'))