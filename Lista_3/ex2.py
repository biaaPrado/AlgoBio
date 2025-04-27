# Pergunta ao usuário se deseja continuar
resposta = input("Continuar (s/n)? ").strip()

# Verificando a resposta
if resposta.lower() == 's':
    print("OK, continuando...")
elif resposta.lower() == 'n':
    print("OK, parando...")
else:
    print("Erro: Resposta inválida!")
