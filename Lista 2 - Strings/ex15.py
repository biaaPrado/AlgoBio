seq = "ATGCGTA"

seq_complementar = ''

for base in seq:
    if base == 'A':
        seq_complementar += 'T'
    elif base == 'T':
        seq_complementar += 'A'
    elif base == 'C':
        seq_complementar += 'G'
    elif base == 'G':
        seq_complementar += 'C'

print(seq_complementar)
