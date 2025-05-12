def eh_multiplo(a, b):
    multiplo = 'não'
    if(a % b == 0):
        multiplo = 'sim'
    return multiplo

# Entrada do usuário
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("É múltiplo?", eh_multiplo(a, b))
