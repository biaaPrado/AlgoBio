def filtrar_impares(lista):
    return [x for x in lista if x % 2 != 0]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = filtrar_impares(numeros)
print(f"Os números ímpares são: {impares}")
