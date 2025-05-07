def operacoes():
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))

    print(f'''
        A soma destes numeros é {num1 + num2}
        A multiplicação destes numeros é {num1 * num2}
        A divisão destes numeros é {num1 / num2}
        A subtração destes numeros é {num1 - num2}
''')
    
operacoes()