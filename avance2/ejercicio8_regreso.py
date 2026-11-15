# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Descripción: Evalúa los recursos para el regreso de la nave
# y determina si la tripulación puede sobrevivir.
# ============================================================

# Constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_DIA = 1

# Entrada de datos
dias_regreso = int(input("Ingrese los días del viaje de ida: "))
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))

combustible_disponible = int(input("Ingrese el combustible disponible: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# Cálculo de recursos necesarios para el regreso
combustible_requerido = dias_regreso * CONSUMO_COMBUSTIBLE_DIA

oxigeno_requerido = dias_regreso * tripulantes * CONSUMO_OXIGENO_DIA

energia_requerida = dias_regreso * CONSUMO_ENERGIA_DIA

provisiones_requeridas = dias_regreso * tripulantes * CONSUMO_PROVISIONES_DIA

# Verificar si hay combustible suficiente para regresar
if combustible_disponible >= combustible_requerido:

    # Inicializar variables
    dias_transcurridos = 0
    regreso_activo = True

    # Calcular consumo diario según los tripulantes
    consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_DIA
    consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_DIA

    # Simular el regreso día por día
    while dias_transcurridos < dias_regreso and regreso_activo:

        # Verificar recursos antes de cada día
        if (combustible_disponible >= CONSUMO_COMBUSTIBLE_DIA and
            oxigeno_disponible >= consumo_oxigeno and
            energia_disponible >= CONSUMO_ENERGIA_DIA and
            provisiones_disponibles >= consumo_provisiones):

            # Descontar los recursos
            combustible_disponible = combustible_disponible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno_disponible = oxigeno_disponible - consumo_oxigeno
            energia_disponible = energia_disponible - CONSUMO_ENERGIA_DIA
            provisiones_disponibles = provisiones_disponibles - consumo_provisiones

            dias_transcurridos = dias_transcurridos + 1

            print("Día completado:", dias_transcurridos)

        else:
            regreso_activo = False
    # Resultado del regreso
    if regreso_activo:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible_disponible)
        print("Oxígeno restante:", oxigeno_disponible)
        print("Energía restante:", energia_disponible)
        print("Provisiones restantes:", provisiones_disponibles)

    else:
        print("El regreso se interrumpió en el día", dias_transcurridos + 1)

        # Identificar los recursos insuficientes
        if combustible_disponible < CONSUMO_COMBUSTIBLE_DIA:
            print("Combustible insuficiente.")

        if oxigeno_disponible < consumo_oxigeno:
            print("Oxígeno insuficiente.")

        if energia_disponible < CONSUMO_ENERGIA_DIA:
            print("Energía insuficiente.")

        if provisiones_disponibles < consumo_provisiones:
            print("Provisiones insuficientes.")

        print("La tripulación no completó el regreso.")
else:
    print("La tripulación quedó varada en el destino.")

    # Calcular los días de supervivencia
    dias_oxigeno = oxigeno_disponible // (tripulantes * CONSUMO_OXIGENO_DIA)
    dias_energia = energia_disponible // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones_disponibles // tripulantes

    # Mostrar los días disponibles por recurso
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)

     # Determinar la supervivencia estimada
    supervivencia_estimada = dias_oxigeno

    if dias_energia < supervivencia_estimada:
        supervivencia_estimada = dias_energia

    if dias_provisiones < supervivencia_estimada:
        supervivencia_estimada = dias_provisiones

    print("Supervivencia estimada:", supervivencia_estimada, "días")

    # Identificar los recursos limitantes
    print("Recurso(s) limitante(s):")

    if dias_oxigeno == supervivencia_estimada:
        print("Oxígeno")

    if dias_energia == supervivencia_estimada:
        print("Energía")

    if dias_provisiones == supervivencia_estimada:
        print("Provisiones")