seq = 'GGTACGGGCA'
baseG = 0

for base in seq:
    if base == 'G':
        baseG += 1

print("Na sequência", seq, "a base G aparece", baseG, 'vezes')