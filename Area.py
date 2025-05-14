# Crie um programa que define uma função calcular_area_retangulo que recebe dois argumentos,
# comprimento e largura de um retângulo, e retorna a área desse retângulo. Em seguida, o programa deve
# solicitar ao usuário que insira o comprimento e a largura e imprimir a área calculada.

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: ')) 

def area(a1,l1):
    area = (a1*l1)
    return area

print(area(altura,largura))