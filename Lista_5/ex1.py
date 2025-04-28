# Leitura da frase
frase = input("Digite uma frase: ")

# Inicializando o dicionário
dicionario = {}

# Contando os caracteres
for caractere in frase:
    if caractere != " ":  # Ignorando espaços
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1

# Exibindo o dicionário
print(dicionario)
