def string_mais_longa(lista):
    return max(lista, key=len)

# Exemplo de uso
strings = ["maçã", "banana", "laranja", "kiwi"]
mais_longa = string_mais_longa(strings)
print(f"A string mais longa é: {mais_longa}")
