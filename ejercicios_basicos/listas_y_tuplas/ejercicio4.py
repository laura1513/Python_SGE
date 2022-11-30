ganadores = []
for i in range(6):
    print("Introduce un número ganador")
    ganador = input()
    ganadores.append(int(ganador))
ganadores.sort()
print("Los números ganadores son", str(ganadores))