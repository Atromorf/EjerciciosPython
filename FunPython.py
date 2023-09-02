#Iva de una cuenta
  
def iva(amount,vat):  

    if vat==0:
        vat=21
        print("tu monto es: " , amount + amount*vat/100)
    else:
        print("tu monto es: " , amount + amount*vat/100)

amount = int(input("ingresa el monto: "))
vat = int(input("ingresa el iva: "))

print("tu monto total es:", iva(amount, vat))


#Area de un circulo

def circle_area(radius):
    
    pi = 3.1415
    
    circle_area=pi*radius**2
    
    return circle_area

def cilinder_volume(radius, high):
    
    cilinder_volume= circle_area(radius)*high
    return cilinder_volume

radius = int(input("ingresa el radio: "))
high = int(input("ingresa el ancho: "))

print("El area del circulo es: " , circle_area(radius))
print("El volumen del circulo es: " , cilinder_volume(radius, high))

#decimal a binario



def binario(b):
    dec = 0
    for pos, dig in enumerate(b[::-1]):
        dec += int(dig)*2**pos
    return dec

def decimal(d):
    num_bi = 0
    mult = 1
    
    while d != 0:
        num_bi = num_bi + d % 2 * mult
        d //= 2
        mult *= 10
    return num_bi


b = str(input("Ingrese un numero binario: "))
d = int(input("Ingrese un numero decimal: "))

print("El numero en binario es: ", binario(b))
print("El numero en decimal es: ", decimal(d))
