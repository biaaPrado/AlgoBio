# Dicionário de frutas e seus preços
frutas = {
    "maçã": 3.5,
    "banana": 2.0,
    "uva": 6.0,
    "laranja": 4.0,
    "manga": 5.5
}

# Dicionário de compras: frutas e quantidades
compras = {
    "maçã": 2,
    "banana": 5,
    "laranja": 3
}

# Calculando o preço total
total = 0
for fruta, quantidade in compras.items():
    if fruta in frutas:
        total += frutas[fruta] * quantidade

print(f"O valor total da compra é: R$ {total:.2f}")

# Criar um novo dicionário apenas com frutas que custam R$5,00 ou menos
frutas_filtradas = {fruta: preco for fruta, preco in frutas.items() if preco <= 5.0}

# Exibindo o novo dicionário
print("Frutas com preço até R$5,00:", frutas_filtradas)
