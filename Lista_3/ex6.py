# Entrada de dados
numero = int(input("Informe um número: "))

# Verificando se o número é primo
if numero <= 1:
    print(f"O número {numero} não é primo.")
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
