# funciones

def nome_da_funcion (parametro1, parametro2="hola"):
    # Instrucciones de la funcion
    print (parametro1)
    print(parametro2)

nome_da_funcion(3,"hola")
nome_da_funcion(parametro2= 3,parametro1="hola")

def recogerParametrosIndefinidos(mensaxe, veces=1, *maisMensaxes):
    print (mensaxe * veces)
    print(type(maisMensaxes))
    for outraMensaxe in maisMensaxes:
        print(outraMensaxe)


recogerParametrosIndefinidos("ola", 6, 6,7,4,3,34,56,765,)
print("---------------")



def persoa(nome,dni, **maisDatos):
    print("O nome é: "+ nome)
    print("O DNI é: + dni")
    for variable in maisDatos.keys():
        print(maisDatos[variable])

persoa("Manolo","56456456K", edade=44, altura=1.23, ocupado=True)

#si la funcion me devuelve varios parametros y solo quiero recoger uno , seria -> _,variable =funcionSumaMedia(var)
# _,h    h,_   h,h














