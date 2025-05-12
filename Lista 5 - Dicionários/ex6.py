# Exemplo de dicionário
dicionario = {
    "nome": "Ana",
    "idade": 22,
    "cidade": "São Paulo"
}

# Perguntar ao usuário a chave que ele quer verificar
chave = input("Digite a chave que deseja verificar: ")

# Verificar se a chave existe
if chave in dicionario:
    print(f"A chave '{chave}' existe no dicionário!")
else:
    print(f"A chave '{chave}' NÃO existe no dicionário.")
