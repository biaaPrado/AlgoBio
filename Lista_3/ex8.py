# Entrada de dados
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

# Calculando o IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3 (obesidade mórbida)"

# Exibindo o resultado
print(f"O seu IMC é {imc:.2f} e a sua classificação é: {classificacao}")
