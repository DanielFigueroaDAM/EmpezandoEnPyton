class Persoa:

    def __init__(self, nome, dni, edade):
        self.nome=nome
        self.dni = dni
        self.edade = edade

    def comprobarEdade(self,id):
        if id >=0 and id < 100:
            self.edade = id
        else:
            self.edade = 0


p = Persoa("Manuel", "356L",34)

print (p.nome)

class Traballador (Persoa):
    def __init__(self, nome,dni,idade,NUSS, salario, formacion):
        super().__init__(nome,dni,idade)
        self.NUSS = NUSS
        self.salario = salario
        self.formacion = formacion



class Persoa2:
    def __init__(self, nome, dni, idade, **outros):
        self.nome = nome
        self.dni = dni
        self.idade = idade
        
        
class Posto2:
    def __init__(self, tarefa, horario, remuneracion, **outros):
        self.tarefa = tarefa  # corregido error de 'tareja' a 'tarefa'
        self.horario = horario
        self.remuneracion = remuneracion
        
class Traballador2(Persoa2, Posto2):
    def __init__(self, nome, dni, idade, tarefa, horario, remuneracion, NUSS):
        Persoa2.__init__(self, nome=nome, dni=dni, idade=idade)
        Posto2.__init__(self, tarefa=tarefa, horario=horario, remuneracion=remuneracion)
        self.NUSS = NUSS

t = Traballador2("Manuel", "356L",34, "limpiar","8-15", 1200, "56456456K")
print(t)
