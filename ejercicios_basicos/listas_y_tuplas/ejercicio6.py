asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
aprobadas = []
for i in asignaturas:
    print("Introduce la nota que has sacado en", i)
    nota = float(input())
    if nota >= 5:
        aprobadas.append(i)

for i in aprobadas:
    asignaturas.remove(i)
print("Tienes que repetir", str(asignaturas))