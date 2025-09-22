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