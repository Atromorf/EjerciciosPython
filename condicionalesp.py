#programa para la contraseña
contra= input("Dame tu contraseña: ")
conta=input("repite la contraseña: ")
if(contra==conta):
    print("tu contraseña es correcta ")
else:
    print("tu contraseña es incorrecta ")

#programa para numeros pares
nume=input("dame un numero: ")
if int(nume) % 2 == 0:
    print("El numero es par")
else:
    print("El numero no es par")
    
    
#programa de edad y precio    
edad= int(input("dame tu edad: "))
if(edad<4):
    print("su pasaje es gratuito")
elif(edad<=18):
    print("Su costo de entrada es de $110")
elif(edad>18):
    print("Su costo de entrada es de 190")
    
#Palindromos
palabra = input("dame una palabra: ")
if str(palabra) == str(palabra)[::-1] :
    print("Palindromo")
else:
    print("No Palindromo")
