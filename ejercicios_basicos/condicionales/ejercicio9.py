print("Introduce tu edad: ", end="")
edad = int(input())

if (edad < 4):
    print("Entras gratis")
elif (edad >= 4 and edad <= 18):
    print("Tu entrada cuesta 5€")
else:
    print("Tu entrada cuesta 10€")