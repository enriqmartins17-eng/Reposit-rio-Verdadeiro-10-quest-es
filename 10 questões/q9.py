matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Preencha a Valor [{i}][{j}]: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)
media = soma / 9
print(matriz)
print("Média: ", media)