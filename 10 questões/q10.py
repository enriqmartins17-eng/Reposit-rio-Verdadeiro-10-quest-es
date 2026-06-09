notas = []

for i in range(3):
    linha = []
    for j in range(4):
        nota = float(input(f"Aluno {i + 1}, Bimestre {j+1}: "))
        linha.append(nota)
    notas.append(linha)

for i in range(3):
    print(f"Aluno {i+1}")
    print("Notas: ",notas[i])

    media = sum(notas[i]) / 4
    print("Média: ",media)

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")