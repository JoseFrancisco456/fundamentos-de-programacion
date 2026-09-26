import pdb
import time

# ==========================================
# CONFIGURACIÓN Y VARIABLES GLOBALES
# ==========================================

# Indica si queremos ejecutar el modo de depuración con PDB.
modo_debug = False

# Archivos que utilizará el sistema para guardar los avisos (Mínimo 4 archivos .txt exigidos)
archivos = [
    "avisos_maquinas.txt",
    "avisos_limpieza.txt",
    "avisos_agua.txt",
    "avisos_material.txt",
    "Otro_problema.txt",
]


# ==========================================
# FUNCIONES AUXILIARES Y PANTALLAS
# ==========================================


def pantalla_carga(nombre):
  """Muestra una pantalla de carga dinámica estilo barra de progreso (máximo 5 segundos)."""
  print("\nIniciando sistema para", nombre)
  for i in range(11):
        porcentaje = i * 10
        barra = "▓▓▓" * i
        print(f"\r[{barra}] {porcentaje}%", end="")
        time.sleep(0.4)
  print("\nSistema listo.")



def pedir_fecha():
  """Solicita y valida la fecha de operación (Día: 1-31, Mes: 1-12, Año: 2000-2100).
  La retorna como una tupla estructurada (dia, mes, año).
  """
  print("--- Registro de Fecha de Operación ---")

  # Validación de Día (1 a 31)
  while True:
    try:
      dia = int(input("Ingresa el día (1-31): "))
      if 1 <= dia <= 31:
        break
      else:
        print("Error: El día debe estar entre 1 y 31.\n")
    except ValueError:
      print("Error: Debes ingresar un número entero válido.\n")

  # Validación de Mes (1 a 12)
  while True:
    try:
      mes = int(input("Ingresa el mes (1-12): "))
      if 1 <= mes <= 12:
        break
      else:
        print("Error: El mes debe estar entre 1 y 12.\n")
    except ValueError:
      print("Error: Debes ingresar un número entero válido.\n")

  # Validación de Año (2000 a 2100)
  while True:
    try:
      año = int(input("Ingresa el año (2000-2100): "))
      if 2000 <= año <= 2100:
        break
      else:
        print("Error: El año debe estar entre 2000 y 2100.\n")
    except ValueError:
      print("Error: Debes ingresar un número entero válido.\n")

  # Almacenamiento en tupla estructurada Fecha = dia, mes, anio
  Fecha = (dia, mes, año)
  print(f"\nFecha registrada correctamente: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}\n")
  return Fecha


def seleccionar_archivo(opcion):
  """Determina el archivo destino en función de la opción seleccionada."""
  if opcion == 1:
    return "avisos_maquinas.txt"
  elif opcion == 2:
    return "avisos_limpieza.txt"
  elif opcion == 3:
    return "avisos_agua.txt"
  elif opcion == 4:
    return "avisos_material.txt"
  elif opcion == 5:
    return "Otro_problema.txt"
  else:
    return "avisos_material.txt"


# ==========================================
# FUNCIONES DE PERSISTENCIA (MANEJO DE ARCHIVOS)
# ==========================================


def guardar_aviso(archivo, problema, estado, tiempo_solucion, Fecha):
  """Guarda un aviso en un archivo de texto con manejo de excepciones y saltos de línea."""
  try:
    with open(archivo, "a", encoding="utf-8") as documento:
      documento.write("=== AVISO DEL GIMNASIO ===\n")
      documento.write("Problema: " + problema + "\n")
      documento.write("Estado: " + estado + "\n")
      documento.write(
          "Tiempo aproximado: " + str(tiempo_solucion) + " minutos\n"
      )
      documento.write(
          "Fecha: "
          + str(Fecha[0])
          + "/"
          + str(Fecha[1])
          + "/"
          + str(Fecha[2])
          + "\n"
      )
      documento.write("---------------------------\n\n")

    print("\n[OK] Aviso guardado correctamente en el archivo.\n")

  except PermissionError:
    print("\nError: No tienes permisos para modificar el archivo.\n")
  except FileNotFoundError:
    print("\nError: El archivo no fue encontrado.\n")
  except Exception as error:
    print("\nOcurrió un error inesperado al guardar:", error, "\n")


def leer_archivo():
  """Permite al usuario seleccionar y desplegar el contenido de uno de los archivos .txt."""
  print("\nArchivos disponibles:")
  for numero in range(len(archivos)):
    print(f"{numero + 1}. {archivos[numero]}")
  print()

  try:
    opcion = int(input("Selecciona el número de archivo que deseas leer: "))

    if opcion < 1 or opcion > len(archivos):
      print("\nOpción de archivo no válida.\n")
      return

    archivo = archivos[opcion - 1]

    with open(archivo, "r", encoding="utf-8") as documento:
      contenido = documento.read()

      print(f"\n--- Contenido de {archivo} ---")
      if contenido.strip() == "":
        print("El archivo está vacío.\n")
      else:
        print(contenido)

  except FileNotFoundError:
    print("\nError: El archivo no existe aún en el sistema.\n")
  except PermissionError:
    print("\nError: No tienes permisos para leer este archivo.\n")
  except ValueError:
    print("\nError: Debes ingresar un número entero válido.\n")
  except Exception as error:
    print("\nOcurrió un error inesperado al leer:", error, "\n")


def agregar_informacion(Fecha):
  """Anexa una nota o información adicional a un archivo de texto existente."""
  print("\nArchivos disponibles:")
  for numero in range(len(archivos)):
    print(f"{numero + 1}. {archivos[numero]}")
  print()

  try:
    opcion = int(input("Selecciona el archivo para agregar notas: "))

    if opcion < 1 or opcion > len(archivos):
      print("\nOpción no válida.\n")
      return

    archivo = archivos[opcion - 1]
    informacion = input("Escribe la información que deseas agregar: ")

    with open(archivo, "a", encoding="utf-8") as documento:
      documento.write("--- INFORMACIÓN ADICIONAL ---\n")
      documento.write("Nota: " + informacion + "\n")
      documento.write(
          "Fecha: "
          + str(Fecha[0])
          + "/"
          + str(Fecha[1])
          + "/"
          + str(Fecha[2])
          + "\n"
      )
      documento.write("---------------------------\n\n")

    print("\n[OK] Información anexada correctamente.\n")

  except FileNotFoundError:
    print("\nError: El archivo no existe.\n")
  except PermissionError:
    print("\nError: No tienes permisos para modificar este archivo.\n")
  except ValueError:
    print("\nError: Debes ingresar un número entero válido.\n")
  except Exception as error:
    print("\nOcurrió un error inesperado:", error, "\n")


# ==========================================
# REGISTRO Y LÓGICA PRINCIPAL DE MÓDULOS
# ==========================================


def registrar_aviso(Fecha):
  """Registra un problema validando la categoría, el estado y impidiendo tiempos negativos."""
  print("\n--- Registrar Nuevo Aviso ---")
  print("1. Máquina dañada")
  print("2. Área sucia")
  print("3. Falta de agua")
  print("4. Material dañado")
  print("5. Otro problema\n")

  try:
    opcion = int(input("Selecciona una opción: "))
  except ValueError:
    print("\nError: Debes ingresar un número entero.\n")
    return

  if opcion == 1:
    problema = "Máquina dañada"
    print("\nAVISO: Revisar la máquina de ejercicio.\n")
  elif opcion == 2:
    problema = "Área sucia"
    print("\nAVISO: Se requiere limpieza del área.\n")
  elif opcion == 3:
    problema = "Falta de agua"
    print("\nAVISO: Revisar el suministro de agua.\n")
  elif opcion == 4:
    problema = "Material dañado"
    print("\nAVISO: Retirar y revisar el material dañado.\n")
  elif opcion == 5:
    problema = input("Describe brevemente el problema: ")
    print("\nAVISO: Se requiere atención del personal.\n")
  else:
    print("\nOpción no válida.\n")
    return

  print("¿Cuál es el estado del problema?")
  print("1. Pendiente")
  print("2. En proceso")
  print("3. Resuelto\n")

  try:
    estado_opcion = int(input("Selecciona el estado: "))
  except ValueError:
    print("\nError: Debes ingresar un número entero.\n")
    return

  if estado_opcion == 1:
    estado = "Pendiente"
  elif estado_opcion == 2:
    estado = "En proceso"
  elif estado_opcion == 3:
    estado = "Resuelto"
  else:
    estado = "No especificado"

  # Validar que si el problema está Resuelto no pida tiempo (es 0)
  # Y si está Pendiente o En proceso no permita tiempos negativos (< 0)
  if estado == "Resuelto":
    tiempo_solucion = 0
  else:
    while True:
      try:
        tiempo_solucion = int(
            input("Tiempo aproximado de solución en minutos: ")
        )
        if tiempo_solucion >= 0:
          break
        else:
          print("Error: El tiempo de solución no puede ser negativo.\n")
      except ValueError:
        print("Error: Debes ingresar un número entero válido.\n")

  archivo = seleccionar_archivo(opcion)

  # Punto de depuración técnica con PDB si modo_debug está activo
  if modo_debug:
    pdb.set_trace()

  # Guardar en el archivo de texto
  guardar_aviso(archivo, problema, estado, tiempo_solucion, Fecha)

  # Resumen en pantalla
  print("--- Reporte Generado ---")
  print("Problema:", problema)
  print("Estado:", estado)
  print("Tiempo aproximado:", tiempo_solucion, "minutos")
  print("Fecha:", f"{Fecha[0]}/{Fecha[1]}/{Fecha[2]}")
  print("Archivo de destino:", archivo)
  print("----------------------------\n")


def mostrar_menu():
  """Presenta el menú de opciones estructurado en formato de matriz."""
  menu = [
      ["1", "Registrar aviso"],
      ["2", "Leer archivos"],
      ["3", "Agregar información"],
      ["4", "Salir"],
  ]

  print("\n--- Menú Principal ---")
  for fila in menu:
    print(f"{fila[0]}. {fila[1]}")
  print()


# ==========================================
# BUCLE PRINCIPAL DE EJECUCIÓN (MAIN)
# ==========================================

while True:

  nombre = input("Ingresa tu nombre o nickname: ")

  # Bienvenida dinámica usando operadores de cadenas (Requerimiento 2)
  bienvenida = (
      "Bienvenido/a " + nombre + " al Sistema de Avisos del Gimnasio!"
  )
  print("\n" + bienvenida)

  # Pantalla de carga dinámica (Requerimiento 3)
  pantalla_carga(nombre)

  # Solicitud y captura estructurada de Fecha (Requerimiento 6)
  Fecha = pedir_fecha()

  salir_inicio = False

  while not salir_inicio:

    mostrar_menu()

    # CONTROL DE INACTIVIDAD DE 10 MINUTOS (600 SEGUNDOS) USANDO UN CICLO FOR
    # Requerimiento 5 de la Guía Evaluativa
    tiempo_inicio = time.time()
    opcion_menu = None

    # Simula medición en rangos de 1 segundo hasta completar los 600 s (10 min)
    for segundo in range(600):
      # Si han pasado más de 10 minutos reales sin interactuar:
      if time.time() - tiempo_inicio >= 600:
        print("\n\n[INACTIVIDAD DETECTADA] Han transcurrido 10 minutos sin uso.")
        respuesta_inactiva = (
            input("¿Deseas continuar en el sistema? (si/no): ").strip().lower()
        )
        if respuesta_inactiva == "si":
          print("\nContinuando en la sesión actual...")
          tiempo_inicio = time.time()  # Reinicia el contador de inactividad
        else:
          print("\nRegresando al menú de inicio del sistema...")
          salir_inicio = True
          break

    # Si se salió por inactividad, salta a la pantalla inicial
    if salir_inicio:
      break

    # Captura de la opción seleccionada por el usuario
    try:
      opcion_menu = int(input("Selecciona una opción del menú: "))
    except ValueError:
      print("\nError: Debes ingresar un número de opción válido.\n")
      continue

    # Navegación entre módulos
    if opcion_menu == 1:
      registrar_aviso(Fecha)
    elif opcion_menu == 2:
      leer_archivo()
    elif opcion_menu == 3:
      agregar_informacion(Fecha)
    elif opcion_menu == 4:
      print("\nSistema finalizado exitosamente.\n")
      salir_inicio = True
    else:
      print("\nOpción no válida.\n")

  # Pregunta para reiniciar todo el programa o salir
  respuesta = (
      input("¿Deseas regresar al inicio del sistema? (si/no): ").strip().lower()
  )

  if respuesta == "no":
    print("\nGracias por utilizar el Sistema de Avisos del Gimnasio. ¡Hasta pronto!\n")
    break
  elif respuesta == "si":
    print("\nRegresando a la pantalla de bienvenida...\n")
  else:
    print("\nRespuesta no reconocida. El programa finalizará por seguridad.\n")
    break