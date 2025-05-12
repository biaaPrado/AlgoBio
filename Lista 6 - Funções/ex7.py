import math

# Função fatorial (do exercício 1)
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Função para calcular sen(x) com série de Taylor
def seno_taylor(x, termos=50):
    seno = 0
    for n in range(termos):
        termo = ((-1)**n * x**(2*n + 1)) / fatorial(2*n + 1)
        seno += termo
    return seno

# Função para calcular cos(x) com base na identidade trigonométrica
def cosseno_por_identidade(seno_valor):
    valor = 1 - seno_valor**2
    return math.sqrt(max(0, valor))

# Entrada do usuário
x = float(input("Digite o valor de x (em radianos): "))

# Cálculos
sen_x = seno_taylor(x)
cos_x = cosseno_por_identidade(sen_x)

# Resultados
print(f"sen({x}) ≈ {sen_x}")
print(f"cos({x}) ≈ {cos_x}")
print(f"sen²({x}) + cos²({x}) ≈ {sen_x**2 + cos_x**2}")
