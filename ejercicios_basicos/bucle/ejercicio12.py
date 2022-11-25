print("Introduce una frase: ", end="")
frase = input()
print("Introduce una letra: ", end="")
letra = input()
cont = 0

for i in frase:
    if i == letra:
        cont += 1
print("La letra ", letra, " aparece ", cont, " veces en la frase: ", frase)