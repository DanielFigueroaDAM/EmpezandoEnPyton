
# LAMBDAS
# Las lambdas son funciones anonimas, es decir, funciones sin nombre
# Se utilizan para funciones sencillas y de una sola linea
# Sintaxis: lambda parametros: expresion
# Ejemplo:
suma = lambda x, y: x + y
print(suma(5, 3))  # Output: 8

# Otro ejemplo
lista_estudiantes =[("Juan", 4.2), ("Ana", 3.5), ("Luis", 4.8), ("Marta", 2.9)]

lista_ordenada = sorted(lista_estudiantes, key= lambda estudiante: estudiante[1])  # Ordena por la nota (segundo elemento de la tupla)
print (lista_ordenada) #¿Esto porque funciona?
# Funciona porque la funcion sorted necesita una funcion que le diga como ordenar los elementos de la lista,
# en este caso le pasamos una lambda que recibe un estudiante (una tupla) y devuelve el segundo elemento de la tupla (la nota)
# De esta forma, sorted puede ordenar la lista de estudiantes por la nota

# Otro ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Queremos filtrar los numeros pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Output: [2, 4, 6, 8, 10]

# Otro ejemplo con bucle for y lambda
cuadrados = [ (lambda x: x**2)(x) for x in range(10)]
print(cuadrados)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

