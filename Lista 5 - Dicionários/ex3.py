# Lendo as informações do aluno
nome = input("Digite o nome do aluno: ")
ra = input("Digite o RA do aluno: ")
media_final = float(input("Digite a média final do aluno: "))

# Armazenando as informações no dicionário
aluno = {
    "Nome": nome,
    "RA": ra,
    "Média Final": media_final
}

# Determinando a situação do aluno pelas regras da UNIFESP
if media_final >= 6.0:
    situacao = "Aprovado"
elif 3.0 <= media_final < 6.0:
    situacao = "Exame"
else:
    situacao = "Reprovado"

# Exibindo as informações
print("\nInformações do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print(f"Situação: {situacao}")
