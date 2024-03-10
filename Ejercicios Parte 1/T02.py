print("1 = Triángulo")
print("2 = Cuadrado")
print("3 = Círculo")

opcion = int(input("Elija el polígono de su elección: "))

if opcion == 1:
    # Triángulo
    altura = float(input("Ingrese la altura del triángulo: "))
    base = float(input("Ingrese la base del triángulo: "))
    
    area = 0.5 * base * altura
    perimetro = 3 * base  # Asumiendo que es un triángulo equilátero

    print("\nEl área del triángulo es: ", area)
    print("El perímetro del triángulo es: ", perimetro)

elif opcion == 2:
    # Cuadrado
    lado = float(input("Ingrese el lado del cuadrado: "))
    
    area = lado ** 2
    perimetro = 4 * lado

    print("\nEl área del cuadrado es: ", area)
    print("El perímetro del cuadrado es: ", perimetro)

elif opcion == 3:
    # Círculo
    radio = float(input("Ingrese el radio del círculo: "))
    
    area = 3.1416 * radio ** 2
    perimetro = 2 * 3.1416 * radio

    print("\nEl área del círculo es: ", area)
    print("El perímetro del círculo es: ", perimetro)

else:
    print("Por favor, ingrese uno de los números válidos (1, 2 o 3).")
