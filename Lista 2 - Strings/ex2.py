seq = input("Digite uma sequência de DNA:")

if 'AG' in seq: 
    seq_repetida = ""
    for i in range(5):
        seq_repetida += seq
    print("Sequência repetida:", seq_repetida)
else:
    print("A sequência não contém 'AG'.")