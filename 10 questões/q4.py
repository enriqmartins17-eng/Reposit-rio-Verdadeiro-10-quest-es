matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Preencha a Valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        soma += valor

print("Total somado: ",soma)