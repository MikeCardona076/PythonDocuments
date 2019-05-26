def Mike():
    frase="El cielo es azul"
    vocales = ['a', 'e', 'i', 'o', 'u','E']
    totalVocales = 0

    for letra in frase:
        if letra in vocales:
            totalVocales += 1
    print("Vocales")   
    print(totalVocales)   
        
Mike()

def Cham():
    frase="El cielo es azul"
    vocales =['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'] 
    consonantes = 0

    for letra in frase:
        if letra in vocales:
            consonantes += 1
    print("Consonantes")   
    print(consonantes)  
Cham()