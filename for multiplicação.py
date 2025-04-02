#Utilize um loop for para calcular o produto dos números de 1 a 5.

resultado = 1
for i in range(1,6):
    print(f"{resultado} x {i} = {resultado*i}")
    resultado *= i