# maior_numero.py
# Programa para determinar o maior número entre 8 valores

numeros = []  # Lista para armazenar os valores

# Solicita 8 valores ao usuário
for i in range(8):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

# Determina o maior número
maior = max(numeros)

# Exibe o resultado
print(f"\nOs números digitados foram: {numeros}")
print(f"O maior número é: {maior}")
