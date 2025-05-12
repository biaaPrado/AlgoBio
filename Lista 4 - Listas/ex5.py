# Inicializando a lista de médias
medias = []
alunos_acima_7 = 0

# Lendo as notas de 5 alunos
for i in range(5):
    print(f"Notas do {i+1}º aluno:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        notas.append(nota)
    
    # Calculando a média do aluno
    media = sum(notas) / len(notas)
    medias.append(media)
    
    # Contando os alunos com média >= 7.0
    if media >= 7.0:
        alunos_acima_7 += 1

# Exibindo os resultados
print(f"Lista de médias dos alunos: {medias}")
print(f"Número de alunos com média >= 7.0: {alunos_acima_7}")
