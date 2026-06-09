matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Preencha a Valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print("Diagonal: ")
for i in range(3):
    print(matriz[i][i])
    soma += (matriz[i][i])

print("Soma da diagonal principal: ", soma)