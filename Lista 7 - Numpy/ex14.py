import numpy as np

def main():
    a = np.arange(12)
    b = np.arange(12, 22)  # exemplo de segundo array de 10 elementos
    print("Array original a (12 el):", a)
    print("Transformado em 3x4:\n", a.reshape((3, 4)))
    
    # concatenar a e b em um único 1D
    c = np.concatenate((a, b))
    print("Segundo array b (10 el):", b)
    print("Concatenado a + b:", c)

if __name__ == "__main__":
    main()
