numeros = [] 

while True:
    
    num = int(input("Digite um número inteiro (0 para sair): "))
        
    if num == 0:
        break

    numeros.append(num)


soma = sum(numeros)
quantidade = len(numeros)
media = soma/quantidade

print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")