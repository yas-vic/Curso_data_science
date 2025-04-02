#Utilize um loop for para imprimir os números de 1 a 20, pulando os múltiplos de 3.

for i in range (1,21):
    if i % 3 == 0:
        continue
    else:
        print(i)