# Crie uma função que receba um horário e imprima "Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.

def saudacao():
    horario = int(input('Que horas são? '))
    if horario >= 6 and horario <= 12:
        print('Bom dia')
    elif horario >= 13 and horario <= 18:
        print('Boa tarde')
    else:
        print('Boa noite')

saudacao()