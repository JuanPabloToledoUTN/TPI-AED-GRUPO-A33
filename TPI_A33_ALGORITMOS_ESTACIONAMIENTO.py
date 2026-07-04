# ==========================================================
# TRABAJO FINAL INTEGRADOR
# GESTIÓN DE ESTACIONAMIENTO
# UTN FRRe - Algoritmos y Estructuras de Datos
# Grupo A33
# ==========================================================

# -------------------- CONSTANTES --------------------

CAPACIDAD_MAXIMA = 50
TARIFA_POR_HORA = 1000

# -------------------- VARIABLES GLOBALES --------------------

vehiculos = []

vehiculos_atendidos = 0

espacios_ocupados = 0

recaudacion_total = 0

acumulador_tiempo = 0


# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def leer_opcion():

    while True:

        try:

            opcion = int(input("\nSeleccione una opción: "))

            if 1 <= opcion <= 4:

                return opcion

            else:

                print("ERROR: La opción debe estar entre 1 y 4.")

        except ValueError:

            print("ERROR: Debe ingresar un número.")


def ingresar_patente():

    while True:

        patente = input("Ingrese la patente: ").upper().strip()

        if patente == "":

            print("ERROR: Debe ingresar una patente.")

        else:

            return patente


def ingresar_hora():

    while True:

        try:

            hora = int(input("Ingrese la hora (0-23): "))

            if 0 <= hora <= 23:

                return hora

            else:

                print("ERROR: Hora inválida.")

        except ValueError:

            print("ERROR: Debe ingresar un número.")


# ==========================================================
# FUNCIONES DE BÚSQUEDA
# ==========================================================

def buscar_vehiculo(patente):

    for i in range(len(vehiculos)):

        if vehiculos[i]["patente"] == patente:

            return i

    return -1


# ==========================================================
# MENÚ
# ==========================================================

def mostrar_menu():

    print("\n===================================")
    print("     SISTEMA DE ESTACIONAMIENTO")
    print("===================================")
    print("1 - Registrar ingreso")
    print("2 - Registrar egreso")
    print("3 - Mostrar estadísticas")
    print("4 - Salir")
    print("===================================")


# ==========================================================
# CÁLCULO DEL IMPORTE
# ==========================================================

def calcular_importe(tiempo):

    return tiempo * TARIFA_POR_HORA
    # ==========================================================
# REGISTRAR INGRESO
# ==========================================================

def registrar_ingreso():

    global espacios_ocupados

    print("\n========== REGISTRO DE INGRESO ==========")

    if espacios_ocupados >= CAPACIDAD_MAXIMA:

        print("ERROR: El estacionamiento está completo.")
        return

    patente = ingresar_patente()

    if buscar_vehiculo(patente) != -1:

        print("ERROR: Ese vehículo ya se encuentra dentro del estacionamiento.")
        return

    hora_ingreso = ingresar_hora()

    vehiculo = {

        "patente": patente,

        "hora": hora_ingreso

    }

    vehiculos.append(vehiculo)

    espacios_ocupados += 1

    print("\nIngreso registrado correctamente.")

    print("----------------------------------------")

    print("Patente:", patente)

    print("Hora de ingreso:", hora_ingreso)

    print("Espacios ocupados:", espacios_ocupados)

    print("Espacios disponibles:",
          CAPACIDAD_MAXIMA - espacios_ocupados)

    print("----------------------------------------")


# ==========================================================
# MOSTRAR VEHÍCULOS ESTACIONADOS
# ==========================================================

def mostrar_vehiculos():

    print("\n========== VEHÍCULOS DENTRO DEL ESTACIONAMIENTO ==========")

    if len(vehiculos) == 0:

        print("No hay vehículos estacionados.")
        return

    for i in range(len(vehiculos)):

        print("----------------------------------------")

        print("Vehículo", i + 1)

        print("Patente:", vehiculos[i]["patente"])

        print("Hora de ingreso:", vehiculos[i]["hora"])

    print("----------------------------------------")
    # ==========================================================
# REGISTRAR EGRESO
# ==========================================================

def registrar_egreso():

    global espacios_ocupados
    global vehiculos_atendidos
    global recaudacion_total
    global acumulador_tiempo

    print("\n========== REGISTRO DE EGRESO ==========")

    if len(vehiculos) == 0:

        print("No hay vehículos dentro del estacionamiento.")
        return

    patente = ingresar_patente()

    posicion = buscar_vehiculo(patente)

    if posicion == -1:

        print("ERROR: La patente no se encuentra registrada.")
        return

    hora_ingreso = vehiculos[posicion]["hora"]

    print("Hora de ingreso:", hora_ingreso)

    hora_salida = ingresar_hora()

    while hora_salida < hora_ingreso:

        print("ERROR: La hora de salida no puede ser menor a la hora de ingreso.")

        hora_salida = ingresar_hora()

    tiempo_permanencia = hora_salida - hora_ingreso

    importe = calcular_importe(tiempo_permanencia)

    print("\n============== TICKET ==============")

    print("Patente:", patente)

    print("Hora de ingreso:", hora_ingreso)

    print("Hora de salida:", hora_salida)

    print("Tiempo de permanencia:", tiempo_permanencia, "hora(s)")

    print("Importe a pagar: $", importe)

    print("====================================")

    vehiculos.pop(posicion)

    espacios_ocupados -= 1

    vehiculos_atendidos += 1

    acumulador_tiempo += tiempo_permanencia

    recaudacion_total += importe

    print("\nEgreso registrado correctamente.")

    print("Espacios ocupados:", espacios_ocupados)

    print("Espacios disponibles:",
          CAPACIDAD_MAXIMA - espacios_ocupados)


# ==========================================================
# MOSTRAR RECAUDACIÓN
# ==========================================================

def mostrar_recaudacion():

    print("\n========== RECAUDACIÓN ==========")

    print("Total recaudado: $", recaudacion_total)

    print("================================")
    # ==========================================================
# MOSTRAR ESTADÍSTICAS
# ==========================================================

def mostrar_estadisticas():

    print("\n========== ESTADÍSTICAS ==========")

    espacios_disponibles = CAPACIDAD_MAXIMA - espacios_ocupados

    porcentaje_ocupacion = (
        espacios_ocupados * 100
    ) / CAPACIDAD_MAXIMA

    if vehiculos_atendidos > 0:

        promedio_permanencia = (
            acumulador_tiempo /
            vehiculos_atendidos
        )

    else:

        promedio_permanencia = 0

    print("Vehículos atendidos:", vehiculos_atendidos)

    print("Vehículos actualmente estacionados:",
          espacios_ocupados)

    print("Espacios disponibles:",
          espacios_disponibles)

    print("Porcentaje de ocupación:",
          round(porcentaje_ocupacion, 2), "%")

    print("Tiempo promedio de permanencia:",
          round(promedio_permanencia, 2), "hora(s)")

    print("Recaudación total: $",
          recaudacion_total)

    mostrar_vehiculos()


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    opcion = 0

    while opcion != 4:

        mostrar_menu()

        opcion = leer_opcion()

        if opcion == 1:

            registrar_ingreso()

        elif opcion == 2:

            registrar_egreso()

        elif opcion == 3:

            mostrar_estadisticas()

        elif opcion == 4:

            print("\n===================================")
            print(" Fin del programa")
            print(" Gracias por utilizar el sistema")
            print("===================================")


# ==========================================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":

    main()
    