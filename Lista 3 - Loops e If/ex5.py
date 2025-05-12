# Função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Imprimindo todos os números primos entre 1 e 100
for num in range(1, 101):
    if eh_primo(num):
        print(num, end=" ")
