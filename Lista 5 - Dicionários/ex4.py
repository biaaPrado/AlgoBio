# Lista para armazenar os dicionários das pessoas
pessoas = []

while True:
    # Lendo os dados de uma pessoa
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo (M/F): ")
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    
    # Calculando o IMC
    imc = peso / (altura ** 2)
    
    # Criando o dicionário da pessoa
    pessoa = {
        "Nome": nome,
        "Sexo": sexo,
        "Peso": peso,
        "Altura": altura,
        "IMC": imc
    }
    
    # Adicionando a pessoa à lista
    pessoas.append(pessoa)
    
    # Pergunta se quer continuar
    continuar = input("Deseja cadastrar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break

# a) Quantidade de pessoas cadastradas
quantidade = len(pessoas)

# b) Peso médio
peso_total = sum(p["Peso"] for p in pessoas)
peso_medio = peso_total / quantidade

# c) Altura média
altura_total = sum(p["Altura"] for p in pessoas)
altura_medio = altura_total / quantidade

# d) IMC médio
imc_total = sum(p["IMC"] for p in pessoas)
imc_medio = imc_total / quantidade

# Exibindo os resultados
print(f"\nQuantidade de pessoas cadastradas: {quantidade}")
print(f"Peso médio: {peso_medio:.2f} kg")
print(f"Altura média: {altura_medio:.2f} m")
print(f"IMC médio: {imc_medio:.2f}")
