import math

print("Introduce una lista de números separados por ','")
num = input()
listaNum = num.split(',')
acum = 0.0
acum2 = 0.0
for i in range(len(listaNum)):
    acum += float(listaNum[i])
    acum2 += float(listaNum[i])**2
media = (float(acum)/len(listaNum))
print("La media es de", media)
total = math.sqrt((float(acum2)/len(listaNum)-media**2))
print("La desviación tipica es de", total)
