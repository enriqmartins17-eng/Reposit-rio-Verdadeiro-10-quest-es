matriz = []

for linha in range(3):
    nova = []
    for coluna in range(3):
        valor = int(input("Preencha a Matriz: "))
        nova.append(valor)
    matriz.append(nova)
print(matriz)