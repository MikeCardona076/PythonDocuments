#Programa para cálcular tres triangulos y decir cual es el mayor
T=[]
contador=0
while contador<3:
    l=int(input("Ingresa el lado "))
    h=int(input("Ingresa la altura "))
    t=1/3* l**2 * h
    T.append(t)
    contador=contador+1

if(T[0]>T[1] and T[0]>T[2]):
         print("este es mayor ") 
         print(T[0])

if(T[1]>T[2] and T[1]>T[0]):
          print("este es mayor ")
          print(T[1])
           
if(T[2]>T[1] and T[2]>T[0]):
         print("este es mayor ")
         print(T[2])