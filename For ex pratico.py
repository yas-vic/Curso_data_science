# Crie uma programa que solicite 10 números para o usuário.
# O programa deve somar todos os números múltiplos de 6
# digitados. Se a soma for igual ou maior que 30, o programa
# dever parar e mostrar o resultado da soma.

soma = 0
for i in range (1,11):
    numero = int(input(f'Digite um numero: '))
    if numero % 6 == 0:
        soma += numero
        print(soma)

    if soma >= 30:
        break

print(soma)