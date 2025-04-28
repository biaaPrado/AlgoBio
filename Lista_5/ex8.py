# Lendo o nome do jogador
jogador = input("Nome do jogador: ")

# Lendo o número de partidas
num_partidas = int(input(f"Quantas partidas {jogador} jogou? "))

# Lista para guardar a quantidade de gols em cada partida
gols_por_partida = []

# Lendo os gols de cada partida
for i in range(1, num_partidas + 1):
    gols = int(input(f"Quantos gols na partida {i}? "))
    gols_por_partida.append(gols)

# Criando o dicionário
aproveitamento = {
    "Nome": jogador,
    "Gols": gols_por_partida,
    "Total de Gols": sum(gols_por_partida)
}

# Exibindo o dicionário
print("\nAproveitamento do jogador:")
for chave, valor in aproveitamento.items():
    print(f"{chave}: {valor}")
