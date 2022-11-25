print("Introduce tu lista de la compra separados por comas: ", end="")
productos = input()

cesta = productos.split(",")

for i in cesta:
    print(i)