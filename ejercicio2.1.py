


def apartado1():
    for indice in range(11,20):
        print(indice)

apartado1()

def apartado2():
    amigos = ["Cristian", "David", "ChatGP","Copilot", "Heids"]
    for amigo in amigos:
        print(amigo)

apartado2()

def apartado3():
    lista =[]
    for indice in range(0,5):
        valor = input()
        lista.append(valor)

    for l in  lista:
        print(l)

apartado3()

def apartado5():
    lista = []
    cantidad = input("Dime cuantos amigos quieres meter")
    for indice in range(0,int(cantidad)):
        valor = input()
        lista.append(valor)

    for l in  lista:
        print(l)

apartado5()