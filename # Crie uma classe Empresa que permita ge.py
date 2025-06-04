# Crie uma classe Empresa que permita gerenciar funcionários. Os funcionários devem ter informações
# como nome, cargo e salário. A empresa deve ser capaz de adicionar, remover e listar funcionários.

class Empresa:
    def __init__ (self,nome,porte,CNPJ):
        self.nome = nome
        self.porte = porte
        self.CNPJ = CNPJ
        self.funcionarios=[
            {
            'nome':'Yasmin','cargo':'CEO','salario':5000
        }
        ]

    def adicionar(self):
        nome = input(f'Digite o nome do funcionario: ')
        cargo = input(f'Digite o cargo do funcionario: ')
        salario = float(input(f'Digite o salario do funcionario: '))
        novo_funcionario = {
            'nome':nome,'cargo':cargo,'salario':salario
        }
        self.funcionarios.append(novo_funcionario)
        print(self.funcionarios)

    def demitir(self):
        for i in range(len(self.funcionarios)):
            print(f' {i} - {self.funcionarios[i]['nome']}')
        escolha_usuario = int(input('Digite o numero do funcionario: '))
        self.funcionarios.pop(escolha_usuario)
        print(self.funcionarios)
        
        
    def listar(self):
        print(self.funcionarios)
        

empresa1= Empresa('AX LTDA','médio','52.6272.562/0271-12')

empresa1.adicionar()
empresa1.demitir()
empresa1.listar()
