def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Entrada do usuário
num = int(input("Digite um número inteiro para calcular o fatorial: "))
print("Fatorial de", num, "é", fatorial(num))
