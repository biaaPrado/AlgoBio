import numpy as np

def taylor_seno(x, termos=20):
    soma = 0.0
    for n in range(termos):
        num = (-1)**n * x**(2*n + 1)
        den = np.math.factorial(2*n + 1)
        soma += num / den
    return soma

def main():
    x = float(input("Digite x (radianos) para aproximar sen(x): "))
    aprox = taylor_seno(x, termos=20)
    print(f"Aproximação de sen({x}) com 20 termos:", aprox)

if __name__ == "__main__":
    main()
