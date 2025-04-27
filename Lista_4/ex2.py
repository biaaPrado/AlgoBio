# Leitura da primeira lista
lista1 = []
n1 = int(input("Quantos elementos você deseja na primeira lista? "))
for i in range(n1):
    lista1.append(input(f"Digite o {i+1}º elemento da primeira lista: "))

# Leitura da segunda lista
lista2 = []
n2 = int(input("Quantos elementos você deseja na segunda lista? "))
for i in range(n2):
    lista2.append(input(f"Digite o {i+1}º elemento da segunda lista: "))

# Gerando a terceira lista com elementos das duas primeiras
lista3 = lista1 + lista2

# Exibindo a terceira lista
print("A terceira lista é:", lista3)
