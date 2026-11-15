# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Descripción: Simula las actividades de exploración científica.
# ============================================================

# Constantes
from unittest import case


ENERGIA_TERRENO = 8
PUNTOS_TERRENO = 10

ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20

ENERGIA_OBSERVACION = 5
PUNTOS_OBSERVACION = 8

# Entrada de datos
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# Inicialización de contadores y acumuladores
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0

# Variable para controlar la exploración
exploracion_activa = True

# Menú de exploración científica
while exploracion_activa:
    
    print("\n--- MENÚ DE EXPLORACIÓN ---")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Digite una opción: "))

    match opcion:
        case 1:
            if energia_disponible >= ENERGIA_TERRENO:
                energia_disponible = energia_disponible - ENERGIA_TERRENO
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_TERRENO

                print("Actividad realizada: Analizar terreno.")
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 2:
            if energia_disponible >= ENERGIA_MUESTRA and provisiones_disponibles >= PROVISIONES_MUESTRA:
                energia_disponible = energia_disponible - ENERGIA_MUESTRA
                provisiones_disponibles = provisiones_disponibles - PROVISIONES_MUESTRA

                actividades_realizadas = actividades_realizadas + 1
                muestras_recolectadas = muestras_recolectadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_MUESTRA

                print("Actividad realizada: Recolectar muestra.")
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 3:
            if energia_disponible >= ENERGIA_OBSERVACION:
                energia_disponible = energia_disponible - ENERGIA_OBSERVACION
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_OBSERVACION

                print("Actividad realizada: Realizar observación.")
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 4:
            exploracion_activa = False

        case _:
            print("Opción no válida.")


# Resumen final de la exploración
print("\n--- RESUMEN DE EXPLORACIÓN ---")
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia_disponible)
print("Provisiones restantes:", provisiones_disponibles)