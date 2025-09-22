# Sentencias condicionais

n1 = 7
n2 = 8


if n1>n2:
    print("n1 es el mas grande")
else:
    print("n2 es mayor")

if n2>n1:
    print("n2 es el mayor")
elif n2 == n1:
    print("son iguales")

vehiculoTipo = "Coche" if n1<=3 else "Moto"


# bucles
a=0
while a<n1:
    print(a)
    a=a+1
print("---------------------")
numeros = [1,3,4,5,6,4,3,2]

for numero in numeros:
    print(numero)
print("---------------------")
for indice in range(5):
    print(indice)

print("---------------------")
for indice in range(1,7,2): # Del 1 al 7 saltando de 3 en 3.
    print(indice)

