# Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

dicionario = {
    'nome' : 'yasmin',
    'idade': 25,
    'altura' : 1.63
}

for chave,valor in dicionario.items():
    print(chave,valor)