#numeros impares

num = int(input("Introduce un número entero positivo: "))
for i in range(1, num+1, 2):
    print(i, end=", ")

print("\n")

#cuenta atras

nume = int(input("Introduce un número entero positivo: "))
for i in range(nume, -1, -1):
    print(i, end=", ")

print("\n")

#tabla de multiplicar

numero=int(input("Introduce un numero entero: "))
for i in range(1, 11):
    print(f'{i} x {numero}={i*numero}')
    
print("\n")

#triangulo con numeros
n = int(input("Introduce la altura del triángulo: "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

print("\n")

#numero de letras

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

print("\n")

#bitacora bancaria

saldo = 0
print ("Escriba la bitacora de operaciones: ")
while True:
    s = input()
    if not s:
        break
    datos = s.split(" ")
    operacion = datos[0]
    monto = int(datos[1])
    if operacion=="D":
        saldo+=monto
    elif operacion=="R":
        saldo-=monto
    else:
        pass
print (saldo)

print("\n")

#arbol navideño

num=int(input("introduce la altura de tu arbol: "))

for i in range(num):
 print((' ' * (num - i - 1)+ "*" *(2 * i + 1)).center(num))

for leg in range(int(num/2)):
 print((' '*int(num-num/4)+'|'*int(num/2)).center(num))
 


#arbol navidad 2
 
 n = int (input ("Introduzca un número entero: "))
for x in range(1,n+1):
    print(' '*(n-x)+'*'*(x*2-1))
b=1
while b<=n:
    print(' '*(n-1)+'||')
    b+=1   












