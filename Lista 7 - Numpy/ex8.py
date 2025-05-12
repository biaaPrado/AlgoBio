import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])
    produto = np.dot(A, B)
    print("A =\n", A)
    print("B =\n", B)
    print("A · B =\n", produto)

if __name__ == "__main__":
    main()
