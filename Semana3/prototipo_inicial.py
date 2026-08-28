while True:

    print("Sistema de avisos del gimnasio ")
    print("1. Máquina dañada")
    print("2. Área sucia")
    print("3. Falta de agua")
    print("4. Material dañado")
    print("5. Otro problema")
    print("6. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        problema = "Máquina dañada"
        print("AVISO: Revisar la máquina de ejercicio.")

    elif opcion == 2:
        problema = "Área sucia"
        print("AVISO: Se requiere limpieza del área.")

    elif opcion == 3:
        print("AVISO: Revisar el suministro de agua.")
        problema = "Falta de agua"
    elif opcion == 4:
        problema = "Material dañado"
        print("AVISO: Retirar y revisar el material dañado.")

    elif opcion == 5:
        problema = input("Describe brevemente el problema: ")

        print("AVISO: Se requiere atención del personal.")
        print("Problema reportado:", problema)

    elif opcion == 6:
        print("Sistema finalizado.")
        break

    else:
        print("Opción no válida.")
        continue

    print("¿Cuál es el estado del problema?")
    print("1. Pendiente")
    print("2. En proceso")
    print("3. Resuelto")

    estado_opcion = int(input("Selecciona el estado: "))

    if estado_opcion == 1:
        estado = "Pendiente"

    elif estado_opcion == 2:
        estado = "En proceso"

    elif estado_opcion == 3:
        estado = "Resuelto"

    else:
        estado = "No especificado"

    tiempo = int(input("Tiempo aproximado de solución (minutos): "))

    print(" Reporte del problema ")
    print("Problema:", problema)
    print("Estado:", estado)
    print("Tiempo aproximado:", tiempo, "minutos")