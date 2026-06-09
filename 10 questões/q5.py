matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Preencha a Valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

maior = [0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

print("Maior valor: ",maior)