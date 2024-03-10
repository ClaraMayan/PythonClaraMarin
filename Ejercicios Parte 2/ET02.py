# Función para saludar y pedir datos personales
def saludar():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo_electronico = input("Ingrese su correo electrónico: ")
    print("¡Hola {}, bienvenido!".format(nombre))
    return {'nombre': nombre, 'apellido': apellido, 'correo': correo_electronico, 'cursos': []}

# Función para realizar una operación matemática con dos números ingresados por el usuario
def realizar_operacion_matematica():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operador = input("Ingrese el operador (+, -): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    else:
        resultado = "Operador no válido"
    print("El resultado es:", resultado)

# Función para agregar a una lista un diccionario que tenga (nombre, edad, correo, cursos)
def agregar_a_lista():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    correo = input("Ingrese el correo electrónico: ")
    
    cursos = []
    while True:
        nombre_curso = input("Ingrese el nombre del curso o escriba 'fin' para terminar: ")
        if nombre_curso.lower() == 'fin':
            break
        notas_str = input("Ingrese las notas del curso separadas por espacios: ")
        notas = list(map(float, notas_str.split()))
        cursos.append({"nombre_curso": nombre_curso, "notas": notas})
    
    alumno = {'nombre': nombre, 'edad': edad, 'correo': correo, 'cursos': cursos}
    lista_alumnos.append(alumno)

# Función para calcular el promedio de las notas de un alumno
def calcular_promedio_notas(notas):
    return sum(notas) / len(notas)

# Función para calcular el promedio de notas y agregar las notas finales a una lista
def calcular_promedio_y_agregar_notas_finales():
    for alumno in lista_alumnos:
        notas_finales = []
        for curso in alumno['cursos']:
            notas_finales.append(calcular_promedio_notas(curso['notas']))
        alumno['notas_finales'] = notas_finales

# Función para mostrar listado de alumnos aprobados
def mostrar_alumnos_aprobados():
    print("\nListado de alumnos aprobados:")
    for alumno in lista_alumnos:
        if all(nota >= 10 for nota in alumno['notas_finales']):
            print(alumno['nombre'])

# Función para mostrar listado de alumnos desaprobados
def mostrar_alumnos_desaprobados():
    print("\nListado de alumnos desaprobados:")
    for alumno in lista_alumnos:
        if any(nota < 10 for nota in alumno['notas_finales']):
            print(alumno['nombre'])

# Función para generar una lista de números múltiplos de 2, 5 y 7
def generar_lista_multiplos():
    lista_multiplos = [i for i in range(1, 10**10) if i % 2 == 0 and i % 5 == 0 and i % 7 == 0]
    print("Tamaño de la lista de múltiplos:", len(lista_multiplos))

# Función para obtener el mayor de dos números ingresados por el usuario
def obtener_mayor():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    mayor = max(num1, num2)
    print("El número mayor es:", mayor)

# Lista de alumnos
lista_alumnos = []

# Menú principal
def menu():
    while True:
        print("\nMENU")
        print("1. Saludar y pedir datos personales")
        print("2. Realizar una operación matemática")
        print("3. Agregar a lista un diccionario con datos de un alumno")
        print("4. Calcular el promedio de las notas y agregar las notas finales a una lista")
        print("5. Mostrar listado de alumnos aprobados")
        print("6. Mostrar listado de alumnos desaprobados")
        print("7. Generar una lista de números múltiplos de 2, 5 y 7")
        print("8. Obtener el mayor de dos números ingresados")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            saludar()
        elif opcion == '2':
            realizar_operacion_matematica()
        elif opcion == '3':
            agregar_a_lista()
        elif opcion == '4':
            calcular_promedio_y_agregar_notas_finales()
        elif opcion == '5':
            mostrar_alumnos_aprobados()
        elif opcion == '6':
            mostrar_alumnos_desaprobados()
        elif opcion == '7':
            generar_lista_multiplos()
        elif opcion == '8':
            obtener_mayor()
        elif opcion == '9':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")

# Ejecutar el menú
menu()
