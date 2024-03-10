try:
    num = int(input("Introduce el número: "))
    lista = [1, 2, 3]
    indice = int(input("Introduce un índice para acceder a la lista: "))
    resultado = lista[indice] / num
except ValueError as v_err:
    print("Error: Debes introducir un número válido.", v_err)
except ZeroDivisionError as zd_err:
    print("Error: División por cero no permitida.", zd_err)
except IndexError as i_err:
    print("Error: Índice fuera de rango.", i_err)
# Agrega más bloques except según sea necesario para manejar otros tipos de errores específicos
else:
    print("Operación exitosa.")
finally:
    print("Finalizando programa.")