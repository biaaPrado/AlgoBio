import numpy as np

def main():
    arr_int = np.array([1, 2, 3, 4, 5])
    arr_float = arr_int.astype(np.float64)
    print("Array original (int):", arr_int)
    print("Convertido para float64:", arr_float)

if __name__ == "__main__":
    main()
