ingreso_total = float(input("Ingrese el ingreso total de su hogar: "))

num_gastos = int(input("\nIngrese el número de gastos que desea registrar: "))

total_gastos = 0
for i in range(1, num_gastos + 1):
    gasto = float(input("Ingrese el monto del gasto {}: ".format(i)))
    total_gastos += gasto

print("\nTotal de egresos:", total_gastos)
print("Total de ahorro:", ingreso_total - total_gastos)
