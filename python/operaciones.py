#Calculadora
def Menu():
    print("Escoge una opcion")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")

def operaciones():
    numero1=int(input("Ingresa un numero: "))
    numero2=int(input("Ingresa un numero: "))
    eleccion=int(input("Que operacion?: "))

    if (eleccion==1):
        print(numero1+numero2)
    elif (eleccion==2):
        print(numero1-numero2)
    elif (eleccion==3):
        print(numero1*numero2)
    elif (eleccion==4):
        print(numero1/numero2)

Menu()
operaciones()