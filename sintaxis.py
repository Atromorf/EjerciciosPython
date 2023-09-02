#esto es un comentario de una linea

"""
esto es un comentario de varias lineas

linea1
linea2
linea3
etc
"""

print("hola")
print('hola mundo python')

a="hola soy una cadena"
print(a)
print(len(a))

b="hola alumnos de s171"
print(b[2:5])
print(b[2:])
print(b[:5])
#esto sirve para ver solo una cantidad especifica de caracteres

a1='Andre'
b2='Fonseca'

print(a1+b2) #sin espacios
print(a1,b2) #con espacios
print(f"{a1} {b2}")#con espacios
print("{}{}".format(a1, b2))#sin espacios

txt="\nlinea1 \nlinea2\n"
print(txt)

#3 variables

x="Luci"
y=5
print(x, y)

x=4.5
y="Jhon"
print(x, y)

x1=str('hola cadena')#todo lo que esta en x solo entrara como cadena de caracteres por str
y1=int(7)#solo guardara numero
z1=float(2.58987)#solo guarda numeros con punto decimal
print(x1, y1, z1)

print(type(x1))#para saber que tipo de archivo se guarda ahi
print(type(y1))
print(type(z1))

#4 Solicitud de datos

#q=input("dame tu nombre: ")
#q=str(input("dame tu nombre: "))
#q2=int(input("escribe tu edad: "))
#q3=float(input("calificacion de POO: "))


#4 Operadores, Booleans

print(10>9)
print(10<9)
print(10==9)
print(10>=0)
print(10<=9)
print(10!=9)

b1=1

print(b1<5 and b1>10)
print(b1<5 or b1>10)
print(not(b1<5 and b1>10))






