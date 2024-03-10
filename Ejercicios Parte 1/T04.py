print("\n")
edad = input("¿Eres mayor de edad? (si/no): ")
if edad.lower() == "si":
    a = input("\nIngrese su edad: ")
    print("\n")
else:
    a = "No proporcionado"

ruc = input("¿Tienes RUC? (si/no): ")
if ruc.lower() == "si":
    b = input("\nIngrese su RUC: ")
    print("\n")
else:
    b = "No proporcionado"

nombre_comercial = input("¿Tienes un nombre comercial? (si/no): ")
if nombre_comercial.lower() == "si":
    c = input("\nIngrese el nombre de su comercio: ")
    print("\n")
else:
    c = "No proporcionado"

if edad.lower() == "si" and ruc.lower() == "si" and nombre_comercial.lower() == "si":
    print("\nUsted es apto para abrir un comercio.")
    print("\n")
else:
    print("\nNo es apto para abrir un comercio y estos son sus datos:")
    print("Edad:", a)
    print("RUC:", b)
    print("Nombre Comercial:", c)
    print("\n")
