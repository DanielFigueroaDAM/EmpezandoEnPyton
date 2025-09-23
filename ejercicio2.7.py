

def calcularFactorial(n):
    if n < 0:
        return "Error: El número debe ser no negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return str(factorial)

n = []
x = 0
while True:
    n.append(int(input(f"{x}Introduce números entero no negativo(-1 para salir): ")))
    x = x + 1
    if n[-1] == -1:
        n.pop()
        break

for num in n:
    print(calcularFactorial(num))