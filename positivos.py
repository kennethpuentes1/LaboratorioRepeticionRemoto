contPar=0
x = int(input("Cuantos valores va a poner?"))

if x > 100:
    print("Demasiados valores :P")
else:
    print("Suficientes valores")

for y in range(1,x,1):
    z= int(input("Escriba el numero "))
    
    if z % 2==0:
       contPar= contPar+1
       print("Es par,valores postivos:" ,contPar)
    elif z%2!=0:
        print("Es impar")
        break