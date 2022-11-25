print("Si quieres la pizza vegetariana pulsa 1, si la quieres no vegetariana pulsa 2")
pizza = input()

if (pizza == '1'):
    print("Hay este tipo de ingredientes: Pimiento y tofu. Debes elegir uno")
    ingrediente = input()
    print("Tu pizza es vegetariana y lleva: Mozzarella, tomate y ", ingrediente)
elif (pizza == '2'):
    print("Hay este tipo de ingredientes: Peperoni, Jamón y Salmón. Debes elegir uno")
    ingrediente = input()
    print("Tu pizza NO es vegetariana y lleva: Mozzarella, tomate y ", ingrediente)
else:
    print("Esa opción no existe")