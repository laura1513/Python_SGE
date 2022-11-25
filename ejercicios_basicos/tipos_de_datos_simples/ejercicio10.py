print("Introduce el número de payasos: ", end="")
payasos = int(input())
print("Introduce el número de muñecas: ", end="")
munyecas = int(input())

pesoPayasos = float(payasos*112)
pesoMunyecas = float(munyecas*75)

pesoTotal = float(pesoMunyecas+pesoPayasos)

print("El peso total es de ", pesoTotal, "g")