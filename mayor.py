k=0
y=0
z=0
for x in range(0, 11):
   x=int(input("Digite el numero entero"))
   if x>0:
      k+=1
   elif x<0:
      y+=1
   elif x==0:
      z+=1
   print(k,"Postivos")
   print(y,"Negativos")
   print(z,"Iguales a cero")
