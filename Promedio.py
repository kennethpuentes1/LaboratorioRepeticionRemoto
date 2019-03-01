contador1=0
contador2=0
contador3=0
contador5=int(input("Cuantos numeros va a añadir?"))
while contador1<contador5:
    contador1+=1
    contador2=int(input("Inserte Numero"))
    contador3+=contador2
    prom=contador3/10
print("Suma:",contador3,"Promedio:",prom)
