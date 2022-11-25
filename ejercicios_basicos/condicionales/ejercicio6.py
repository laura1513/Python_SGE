print("Introduce tu nombre: ", end="")
nombre = input()
print("Introduce tu sexo H o M: ", end="")
sexo = input()

if ((sexo == 'H' and nombre.lower() > 'n') or (sexo == 'M' and nombre.lower() < 'm')):
    grupo = 'A'
else:
    grupo = 'B'
print("Perteneces al grupo ", grupo)