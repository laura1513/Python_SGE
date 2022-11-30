print("Introduce una palabra")
palabra = input()
reversa = palabra
palabra = list(palabra)
reversa = list(reversa)
reversa.reverse()
if palabra == reversa:
    print("Es un palindromo")
else:
    print("No es un palindromo")