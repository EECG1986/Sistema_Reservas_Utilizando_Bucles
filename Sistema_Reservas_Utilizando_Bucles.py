# Declara una lista vacía para almacenar las reservas
reservas = []

# Función para realizar una reserva
def realizar_reserva(nombre, numero_personas, fecha, hora):
    # Formatea la reserva y agrega a la lista
    reserva = f"{nombre}-{numero_personas}-{fecha}-{hora}"
    reservas.append(reserva)

# Función para mostrar todas las reservas
def mostrar_reservas():
    print("Reservas actuales:")
    for reserva in reservas:
        print(reserva)

# Función para buscar reservas por nombre
def buscar_reserva(nombre):
    print(f"Reservas de {nombre}:")
    for reserva in reservas:
        if nombre in reserva:
            print(reserva)

# Función para eliminar una reserva por nombre y fecha
def eliminar_reserva(nombre, fecha):
    for reserva in reservas:
        datos_reserva = reserva.split("-")
        if datos_reserva[0] == nombre and datos_reserva[2] == fecha:
            reservas.remove(reserva)
            print(f"Reserva de {nombre} el {fecha} eliminada.")
            return
    print(f"No se encontró una reserva de {nombre} el {fecha}.")

# Ejemplo de uso
realizar_reserva("Juan", 3, "2024-02-18", "18:00")
realizar_reserva("María", 2, "2024-02-20", "19:30")
realizar_reserva("Pedro", 5, "2024-02-22", "20:00")

mostrar_reservas()
buscar_reserva("María")
eliminar_reserva("Juan", "2024-02-18")

mostrar_reservas()



# Lista para almacenar las reservas
reservas = []

# Función para realizar una reserva
def realizar_reserva():
    nombre = input("Ingrese el nombre: ")
    numero_personas = input("Ingrese el número de personas: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    hora = input("Ingrese la hora: ")
    # Validación de la entrada
    if nombre and numero_personas and fecha and hora:
        reserva = f"{nombre}-{numero_personas}-{fecha}-{hora}"
        reservas.append(reserva)
        print("Reserva realizada exitosamente.")
    else:
        print("Error: Todos los campos son requeridos.")

# Función para mostrar todas las reservas
def mostrar_reservas():
    print("Reservas actuales:")
    for reserva in reservas:
        print(reserva)

# Función para buscar reservas por nombre
def buscar_reserva():
    nombre = input("Ingrese el nombre: ")
    if nombre:
        print(f"Reservas de {nombre}:")
        encontrada = False
        for reserva in reservas:
            if nombre in reserva:
                print(reserva)
                encontrada = True
        if not encontrada:
            print(f"No se encontraron reservas de {nombre}.")
    else:
        print("Error: El nombre es requerido.")

# Función para eliminar una reserva por nombre y fecha
def eliminar_reserva():
    nombre = input("Ingrese el nombre: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    if nombre and fecha:
        encontrada = False
        for reserva in reservas:
            datos_reserva = reserva.split("-")
            if datos_reserva[0] == nombre and datos_reserva[2] == fecha:
                reservas.remove(reserva)
                print(f"Reserva de {nombre} el {fecha} eliminada.")
                encontrada = True
                break
        if not encontrada:
            print(f"No se encontró una reserva de {nombre} el {fecha}.")
    else:
        print("Error: Nombre y fecha son requeridos.")

# Bucle principal
while True:
    print("\nMenú:")
    print("1. Realizar reserva")
    print("2. Mostrar todas las reservas")
    print("3. Buscar reserva por nombre")
    print("4. Eliminar reserva")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción: ")
    if opcion == "1":
        realizar_reserva()
    elif opcion == "2":
        mostrar_reservas()
    elif opcion == "3":
        buscar_reserva()
    elif opcion == "4":
        eliminar_reserva()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
