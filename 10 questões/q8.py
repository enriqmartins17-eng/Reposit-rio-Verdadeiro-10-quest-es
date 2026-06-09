matriz = []
pares = 0
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Preencha a Valor [{i}][{j}]: "))
        linha.append(valor)
        if valor % 2 == 0:
            pares += 1 
    matriz.append(linha)
print(matriz)
print("números pares: ",pares)