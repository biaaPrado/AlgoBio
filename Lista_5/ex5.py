alunos = [
    {"nome": "Ana", "turma": "101"},
    {"nome": "Bruno", "turma": "102"},
    {"nome": "Carla", "turma": "101"},
    {"nome": "Daniel", "turma": "103"},
    {"nome": "Eduarda", "turma": "102"}
]

# Inicializar um dicionário vazio para o agrupamento
agrupados = {}

# Percorrer a lista de alunos
for aluno in alunos:
    turma = aluno["turma"]
    
    # Se a turma ainda não está no dicionário, cria uma nova lista
    if turma not in agrupados:
        agrupados[turma] = []
    
    # Adiciona o aluno à lista da turma
    agrupados[turma].append(aluno["nome"])

# Exibir o agrupamento
for turma, nomes in agrupados.items():
    print(f"Turma {turma}: {nomes}")
