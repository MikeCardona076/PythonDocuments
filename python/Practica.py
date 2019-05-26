palabra=input("Escribe una palabra: ")
veces_palabra= int(input("Numero de veces: "))

for recorrido in range(0,veces_palabra):

    if (veces_palabra > 120):
        print("Pedro ", palabra)
    else:
        print(palabra)

    
if (veces_palabra==500):
    print("Hola")

elif(veces_palabra < 100):
    print("Hola Mortales")

else:
    print("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")