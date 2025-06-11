#Crie uma classe Funcionario com nome e salário. 
# Depois, crie Gerente e Programador como classes filhas, e adicione um método especial para cada uma.


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente (Funcionario):
    def contratar (self):
        print(f'{self.nome} está em processo de contratação')

class Programador (Funcionario):
    def programar (self):
        print(f'{self.nome} está programando')

gerente_infinity= Gerente("Gilson",15000)
gerente_infinity.contratar()

programador_infinity= Programador("Adimilson",51000)
programador_infinity.programar()