print("Introduce la cantidad de dinero que introduces: ", end="")
dinero = float(input())
cantidad = 0
for i in range(3):
    dinero = dinero +(dinero * (4/100))
    print("Tu cuenta el año", i+1, "dispone de ", round(dinero, 2))