def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"

# Entrada do usuário
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
print("Resultado:", calculadora(a, b, operacao))
