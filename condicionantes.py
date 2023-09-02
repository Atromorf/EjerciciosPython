from optparse import Option

dia= input("Dia de la semana: ")
if(dia=="lunes"):
    print("OH, no!")
elif(dia=="Viernes"):
    print("Ya casi!!")
elif(dia=="sabado" or dia=="domingo"):
    print("Ahora si se puede descansar")
else: 
    print("A esperar el fin de semana")