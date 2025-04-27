# Inicializando as listas
pares = []
impares = []

# Lendo 20 números inteiros
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exibindo as listas
print("Lista de números pares:", pares)
print("Lista de números ímpares:", impares)
