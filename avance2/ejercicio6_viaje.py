# ============================================================
# Archivo: ejercicio6_viaje.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Descripción: Simula el viaje hacia el destino día por día.
# ============================================================

# Constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_DIA = 1

# Entrada de datos
dias_viaje = int(input("Ingrese la cantidad de días del viaje: "))
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))

combustible_disponible = int(input("Ingrese el combustible disponible: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# Inicialización de variables
dias_transcurridos = 0
viaje_activo = True

# Calcular el consumo diario según los tripulantes
consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_DIA
consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_DIA

# Simulación del viaje día por día
while dias_transcurridos < dias_viaje and viaje_activo:

    # Verificar si hay recursos suficientes para el día
    if (combustible_disponible >= CONSUMO_COMBUSTIBLE_DIA and
        oxigeno_disponible >= consumo_oxigeno and
        energia_disponible >= CONSUMO_ENERGIA_DIA and
        provisiones_disponibles >= consumo_provisiones):

        # Descontar los recursos diarios
        combustible_disponible = combustible_disponible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno_disponible = oxigeno_disponible - consumo_oxigeno
        energia_disponible = energia_disponible - CONSUMO_ENERGIA_DIA
        provisiones_disponibles = provisiones_disponibles - consumo_provisiones

        # Aumentar los días completados
        dias_transcurridos = dias_transcurridos + 1

        # Mostrar los recursos restantes
        print("Día", dias_transcurridos,
              "| Combustible:", combustible_disponible,
              "| Oxígeno:", oxigeno_disponible,
              "| Energía:", energia_disponible,
              "| Provisiones:", provisiones_disponibles)

    else:
        viaje_activo = False

        # Resultado final del viaje
if viaje_activo:
    print("La nave llegó al destino en", dias_transcurridos, "días.")
    print("Combustible restante:", combustible_disponible)
    print("Oxígeno restante:", oxigeno_disponible)
    print("Energía restante:", energia_disponible)
    print("Provisiones restantes:", provisiones_disponibles)

else:
    print("Viaje interrumpido en el día", dias_transcurridos + 1)

    # Identificar los recursos insuficientes
    if combustible_disponible < CONSUMO_COMBUSTIBLE_DIA:
        print("Combustible insuficiente.")

    if oxigeno_disponible < consumo_oxigeno:
        print("Oxígeno insuficiente.")

    if energia_disponible < CONSUMO_ENERGIA_DIA:
        print("Energía insuficiente.")

    if provisiones_disponibles < consumo_provisiones:
        print("Provisiones insuficientes.")

    print("Días completados:", dias_transcurridos)