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

class Persoa3:
    def __init__(self, nome, dni, idade):
        self.setNome(nome)
        self.setDni(dni)
        self.setIdade(idade)


    def setDni(self,dni):
        if type(dni) == str:
            if len(dni) == 9:
                self.dni = dni
            else:
                self.dni = "00000000X"  # opción por defecto si la longitud es >= 9
        else:
            self.dni = "00000000X"

    def getDni(self):
        return self.dni
    def setNome(self,nome):
        if type(nome)==str:
            self.nome = nome
        else:
            self.nome = "Sen nome"
    def getNome(self):
        return self.nome
    def setIdade(self,idade):
        if type(idade)==int:
            if idade>=0 and idade<100:
                self.idade = idade
            else:
                self.idade = 0
        else:
            self.idade = 0
    def getIdade(self):
        return self.idade
    def __str__(self):
        return f"Nome: {self.getNome()}, DNI: {self.getDni()}, Idade: {self.getIdade()}"
    def __eq__(self, other):
        return self.dni == other.dni
    def __ne__(self, other):
        return self.dni != other.dni
    def __len__(self):
        return len(self.nome)

p = Persoa3("Manuel", "356L",34)

p.setDni(345345)



print (p.getDni() == "00000000X")
