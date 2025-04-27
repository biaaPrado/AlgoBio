# Entrada de dados
numero = int(input("Digite um número para verificar se é um número de Armstrong: "))

# Convertendo o número para string para poder acessar seus dígitos
num_str = str(numero)
num_digitos = len(num_str)

# Calculando a soma dos dígitos elevados à potência do número de dígitos
soma = sum(int(digito) ** num_digitos for digito in num_str)

# Verificando se o número é um número de Armstrong
if soma == numero:
    print(f"O número {numero} é um número de Armstrong.")
else:
    print(f"O número {numero} não é um número de Armstrong.")
