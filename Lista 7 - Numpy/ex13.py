import numpy as np

def main():
    a = np.array([2, 4, 6, 8, 10])
    print("Array:", a)
    print("Média:", np.mean(a))
    print("Desvio padrão:", np.std(a))
    print("Soma total:", np.sum(a))

if __name__ == "__main__":
    main()
