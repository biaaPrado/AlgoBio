def maior_palavra(lista):
    maior = lista[0]
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
    return maior

# Entrada do usuário: uma palavra por vez
palavras = []
print("Digite uma palavra por vez. Pressione Enter sem digitar nada para finalizar:")

while True:
    palavra = input("Palavra: ")
    if palavra == "":
        break
    palavras.append(palavra)

# Verifica se a lista não está vazia
if palavras:
    print("Maior palavra:", maior_palavra(palavras))
else:
    print("Nenhuma palavra foi digitada.")
