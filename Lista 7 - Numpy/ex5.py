import numpy as np

def main():
    a = np.array([[10, 20, 30],
                  [40, 50, 60]])
    print("a =\n", a)
    print("a[2ª linha, 3ª coluna]:", a[1, 2])
    print("Primeira linha inteira:", a[0])
    print("Todos os elementos da coluna 2:", a[:, 1])

if __name__ == "__main__":
    main()
