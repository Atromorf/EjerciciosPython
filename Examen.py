import math

n = int(input("Ingresa un numero: "))
if n > 0:
    digitos = int(math.log10(n))+1
elif n == 0:
    digitos = 1
elif n < 0:
    digitos = int(math.log10(-n))+2
print(digitos)