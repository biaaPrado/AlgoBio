seq = "AAGCTA"
nova_seq = ""

for base in seq:
    if base == 'A':
        nova_seq += 'T'
    else: 
        nova_seq += base

print(nova_seq)

#ou 

seq = "AAGCTA"
nova_seq = seq.replace('A', 'T')

print(nova_seq)