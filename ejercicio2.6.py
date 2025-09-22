
n = int(input("Introduce un número entero positivo: "))
acumulador = 0

for i in range(0, n):
    for j in range(0, i+1):
        acumulador = acumulador + j
    print(str(i)+"-"+str(acumulador))
    acumulador = 0


