import random


print("Cuantos numeros quieres en la lista")
n=int(input())
l1 = [random.randint(0,100) for _ in range(n)]
print(l1)
lon=float(len(l1))
print(sum(l1)/lon)


print("cuantos numeros quieres en esta lista")
l=int(input())
L2 = [random.randint(101,200) for _ in range(l)]
print(L2)

print("Cuantos aqui")
m=int(input())
l3= [random.randint(201,300) for _ in range(m)]
print(l3)


