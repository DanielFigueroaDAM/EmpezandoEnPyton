"""Coleccións:

    Listas:
    Tuplas:
    Diccionarios:

"""
#Listas
l = [23, 35, 56, -34, 45]
l2 = [23, 45.6, -15, [2,3,4], "unha cadea"]
l[-1] = "Outra cadea"
print(l[-1])

#Slicing

print(l[2:5])
print(l[:5])
print(l[2:])
print(l[1:6:2]) # de dos en dos
print (l[::-1]) #Invierte la lista

#Tpulas

t = (2,5,4+4j, "un texto") # Las tuplas no son mutables

#t[2] = "Outro texto" Esto da error

t2 = (5,4,3,[2,3,4])
t2[-1][2] = 6
print(t2)

# Diccionarios

d = { 1 : "Un",
      2 : "Dous",
      3 : "Tres",
      4 : "Catro"
}

# len(coleccion) -> devuleve la longitud de la lista.

# Esta es otra manera de de crear una lista
l3 = list((2,3,4,5,6))

t3 = tuple((2,3,4,5,6))

d3 = dict( ( (1,"un"), (2,"dous"), (3,"tres") ) )

l2.append([3,4,5]) # Añade un elemento al final de la lista
l2.extend([6,7,8]) # Añade varios elementos al final de la lista
l2.insert(2,"un elemento") # Inserta un elemento en la posicion 2
l2.count(2) # Cuenta las veces que aparece el elemento 2 en la lista
l2.remove("un elemento") # Elimina el elemento indicado
l2.__len__() # Devuelve la longitud de la lista
l2.index(3,3,7) # Devuelve la posicion del elemento 3 entre las posiciones 3 y 7
l2.pop() # Elimina y devuelve el ultimo elemento de la lista
l2.pop(3) # Elimina y devuelve el elemento en la posicion 3
l2.remove(3) # Elimina la primera ocurrencia del elemento 3
l2.reverse() # Invierte la lista
l3=l2[::-1] # Otra manera de invertir la lista pero creando una nueva y la original no se modifica
l2.sort() # Ordena la lista

