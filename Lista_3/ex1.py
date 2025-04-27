# Função para determinar o tipo de solução
def tipo_solucao(pH):
    if pH > 7 and pH <= 14:
        print("A solução é ácida.")
    elif pH < 7 and pH >= 0:
        print("A solução é básica.")
    elif pH == 7:
        print("A solução é neutra.")
    else:
        print("Valor de pH inválido.")

# Entrada do pH
pH = float(input("Digite o valor do pH da solução: "))

# Chamando a função
tipo_solucao(pH)
