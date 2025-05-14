# Crie uma função chamada concatenar_strings que
# aceita um número variável de strings como argumentos
# posicionais (usando *args). A função deve concatenar
# todas as strings em uma única string e retorná-la.

def concatenar_strings(*args):
    nova_str = ""
    for texto in args:
        nova_str += texto
    return nova_str
    
print (concatenar_strings("Yasmin ","Victoria ","de ","Oliveira"))