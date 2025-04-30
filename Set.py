# # Crie um conjunto vazio chamado frutas e adicione as
# # seguintes frutas a ele: "maçã","banana","uva","laranja"e "morango". Em seguida, imprima o conjunto.

# Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

frutas =  set()
frutas.update(["maçã","banana","uva","laranja","morango","morango"])

if "banana" in frutas:
    print(True)