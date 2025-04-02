# Use o aprendizado desta aula para implementar o for ao projeto.
# Após implementar o sistema de cadastro de senha,
# chegou a hora de entrar no sistema operacional.
# Após ligar o celular, é necessário inserir a senha
# cadastrada.
# São 3 tentativas até o telefone bloquear.
# Se o usuário acertar a senha, escreva a mensagem:
# “bem vindo.”
# Se o usuário errar a senha, escreva a mensagem:
# “Senha incorretar. Você tem x tentativas até o bloqueio.

tentativa = 0
senha = 14156

for i in range (3):
    digite_sua_senha = input(f'Digite sua senha: ')

    if digite_sua_senha == senha:
        print('Bem vindo')
        

    else:
        tentativa += 1
        print(f'Senha incorreta! Você tem {3 - tentativa} tentativas')
        if tentativa >= 3:
            break
        