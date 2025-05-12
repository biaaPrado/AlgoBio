def soma_quadrados(lista):
    return sum(x**2 for x in lista)

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = soma_quadrados(numeros)
print(f"A soma dos quadrados é: {resultado}")
