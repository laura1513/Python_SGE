print("Introduce tu edad: ", end="")
edad = int(input())

if (edad <=0):
    print("Edad mal introducida")
else:
    for i in range(edad):
        print("Has cumplido ", (i+1), " años")