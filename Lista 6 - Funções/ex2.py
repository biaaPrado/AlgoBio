def maxnum(*numeros):
    maior = numeros[0]
    for num in numeros:
        if num > maior:
            maior = num
    return maior

# Entrada do usuário
entrada = input("Digite os números separados por espaço: ")
numeros = tuple(map(int, entrada.split()))
print("Maior número:", maxnum(*numeros))
