def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)

# Entrada do usuário
n = int(input("Digite um número inteiro positivo: "))
print("Soma de 1 até", n, "é", soma_recursiva(n))
