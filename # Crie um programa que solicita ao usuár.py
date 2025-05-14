# Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas
# usando uma função. A função deve receber as três
# notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada.


nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

def media(n1,n2,n3):
    media=(n1+n2+n3)/3
    return media

print(media(nota1,nota2,nota3))