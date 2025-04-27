# Leitura dos 10 números reais
numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Exibindo os números na ordem inversa
print("Os números na ordem inversa são:")
for numero in reversed(numeros):
    print(numero)
