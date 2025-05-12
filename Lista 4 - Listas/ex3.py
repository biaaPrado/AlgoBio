# Lista de temperaturas de Mons
T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Encontrando a menor e maior temperatura
menor_temperatura = min(T)
maior_temperatura = max(T)

# Calculando a temperatura média
temperatura_media = sum(T) / len(T)

# Exibindo os resultados
print(f"A menor temperatura é: {menor_temperatura}°C")
print(f"A maior temperatura é: {maior_temperatura}°C")
print(f"A temperatura média é: {temperatura_media:.2f}°C")
