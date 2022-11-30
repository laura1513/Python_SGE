asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for i in asignaturas:
    print("Introduce la nota que has sacado en", i)
    nota = input()
    notas.append(nota)

for i in range(len(asignaturas)):
    print("En", asignaturas[i], "has sacado", notas[i])