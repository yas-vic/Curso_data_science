# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
# quantidade de números impares.

par = 0
impar = 0

for i in range(1,11):
    num = int(input('Digite 10 numeros: '))
    
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
        
print(f'Há {par} pares')
print(f'Há {impar} impares')


   