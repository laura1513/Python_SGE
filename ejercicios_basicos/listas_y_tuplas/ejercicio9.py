palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for i in vocales:
    cont = 0
    for j in palabra:
        if j == i:
            cont += 1
    print("La vocal " + i + " aparece " + str(cont) + " veces")