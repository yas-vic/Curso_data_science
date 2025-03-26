numero = 48
limite = 1



while limite <= 4:
    adivinhe = int(input('Adivinhe o numero secreto: '))
    if numero > adivinhe:
        print('Numero muito baixo. Continue tentando!')
    
    elif numero < adivinhe:
        print('Numero muito alto. Continue tentando!')
    
    else:
        print('Vc acertou!')
        break
    limite +=1