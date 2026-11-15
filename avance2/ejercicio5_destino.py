# ============================================================
# Archivo: ejercicio5_destino.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Descripción: Selecciona el destino y verifica si la misión
# tiene suficientes recursos para autorizar el lanzamiento.
# ============================================================

# Constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO = 2
CONSUMO_ENERGIA = 5
RESERVA_COMBUSTIBLE = 10
RESERVA_OXIGENO = 5
RESERVA_ENERGIA = 10
RESERVA_PROVISIONES = 3

# Entrada de datos
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))

# Mostrar las opciones de destino
print("Seleccione el destino de la misión:")
print("1. Luna")
print("2. Marte")
print("3. Europa")

opcion_destino = int(input("Digite la opción de destino: "))

# Recursos disponibles


# Selección del destino
match opcion_destino:
    case 1:
        destino = "Luna"
        dias_viaje = 3

    case 2:
        destino = "Marte"
        dias_viaje = 5

    case 3:
        destino = "Europa"
        dias_viaje = 7

    case _:
        print("Opción de destino no válida. La misión no puede planificarse.")

       # Verificar si el destino es válido
if opcion_destino == 1 or opcion_destino == 2 or opcion_destino == 3:

    combustible_disponible = int(input("Ingrese el combustible disponible: "))
    oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
    energia_disponible = int(input("Ingrese la energía disponible: "))
    provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
    
        # Cálculo de recursos requeridos
    combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA

    combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

    oxigeno_requerido = dias_viaje * tripulantes * CONSUMO_OXIGENO + RESERVA_OXIGENO

    energia_requerida = dias_viaje * CONSUMO_ENERGIA + RESERVA_ENERGIA

    provisiones_requeridas = dias_viaje * tripulantes + RESERVA_PROVISIONES

            # Mostrar resumen de la misión
    print("\n--- RESUMEN DE LA MISIÓN ---")
    print("Misión:", nombre_mision)
    print("Destino:", destino)
    print("Tripulantes:", tripulantes)
    print("Duración del viaje de ida:", dias_viaje, "días")

    print("Combustible para llegar:", combustible_ida, "unidades")
    print("Combustible para regresar:", combustible_regreso, "unidades")
    print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
    print("Combustible total requerido:", combustible_total, "unidades")
    print("Oxígeno requerido:", oxigeno_requerido, "unidades")
    print("Energía requerida:", energia_requerida, "unidades")
    print("Provisiones requeridas:", provisiones_requeridas, "unidades")

    # Verificación de recursos
    if (combustible_disponible >= combustible_total and
        oxigeno_disponible >= oxigeno_requerido and
        energia_disponible >= energia_requerida and
        provisiones_disponibles >= provisiones_requeridas):

        print("Lanzamiento autorizado.")

    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")