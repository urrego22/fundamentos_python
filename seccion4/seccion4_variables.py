# =============================================================
# SECCIÓN 4 - Variables
# Fundamentos de Python - GA1-220501093-04-AA1-EV01
# =============================================================

# -------------------------------------------------------------
# 1. CREAR Y USAR UNA VARIABLE
# -------------------------------------------------------------

var = 1
print(var)

# -------------------------------------------------------------
# 2. VARIOS TIPOS EN VARIABLES
# -------------------------------------------------------------

account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

# Combinar texto con variable usando +
version = "3.12.0"
print("Python version: " + version)

# -------------------------------------------------------------
# 3. REASIGNAR VALOR A UNA VARIABLE
# -------------------------------------------------------------

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

# -------------------------------------------------------------
# 4. RESOLVER PROBLEMAS MATEMÁTICOS - Teorema de Pitágoras
# -------------------------------------------------------------

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)       # c = 5.0

# -------------------------------------------------------------
# 5. OPERADORES ABREVIADOS
# -------------------------------------------------------------

x = 10
x += 5        # x = x + 5  --> 15
print(x)

x -= 3        # x = x - 3  --> 12
print(x)

x *= 2        # x = x * 2  --> 24
print(x)

x /= 4        # x = x / 4  --> 6.0
print(x)

x //= 2       # x = x // 2 --> 3.0
print(x)

x **= 3       # x = x ** 3 --> 27.0
print(x)

x %= 5        # x = x % 5  --> 2.0
print(x)


# =============================================================
# LAB 1 - Variables básicas
# =============================================================

var = 1
print(var)

account_balance = 1000.0
client_name = "John Doe"
print(var, account_balance, client_name)

version = "3.12.0"
print("Python version: " + version)

var = var + 1
print(var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("Hipotenusa c =", c)


# =============================================================
# LAB 2 - Variables: un convertidor simple
# =============================================================
#
# Salida Esperada:
# 7.38 millas son 11.88 kilómetros
# 12.25 kilómetros son 7.61 millas
# -------------------------------------------------------------

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


# =============================================================
# LAB 3 - Operadores y expresiones
# =============================================================
#
# Evalúa: 3x³ - 2x² + 3x - 1
#
# Salida esperada:
# y = -1.0
# y = 3.0
# y = -9.0
# -------------------------------------------------------------

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)


# =============================================================
# LAB 4 - Ejercicios de Algoritmos (Gameplay)
# =============================================================
#
# Escenario:
# Usted es un desarrollador de mecánicas de un gameplay.
# Resuelva los 16 algoritmos usando variables y operadores aritméticos.
# -------------------------------------------------------------

# --- Ejercicio 1: Puntaje total de un jugador ---
print("\n=== Ejercicio 1: Puntaje total ===")
nivel1 = int(input("Ingrese los puntos obtenidos en el nivel 1: "))
nivel2 = int(input("Ingrese los puntos obtenidos en el nivel 2: "))
nivel3 = int(input("Ingrese los puntos obtenidos en el nivel 3: "))
puntaje_total = nivel1 + nivel2 + nivel3
print("Puntaje total:", puntaje_total)

# --- Ejercicio 2: Tiempo total de juego en segundos ---
print("\n=== Ejercicio 2: Tiempo total en segundos ===")
horas = int(input("Ingrese las horas jugadas: "))
minutos = int(input("Ingrese los minutos jugados: "))
segundos = int(input("Ingrese los segundos jugados: "))
tiempo_total_segundos = horas * 3600 + minutos * 60 + segundos
print("Tiempo total en segundos:", tiempo_total_segundos)

# --- Ejercicio 3: Daño total causado por un personaje ---
print("\n=== Ejercicio 3: Daño total ===")
ataque1 = int(input("Ingrese el daño del ataque 1: "))
ataque2 = int(input("Ingrese el daño del ataque 2: "))
ataque3 = int(input("Ingrese el daño del ataque 3: "))
danio_total = ataque1 + ataque2 + ataque3
print("Daño total:", danio_total)

# --- Ejercicio 4: Experiencia total ganada ---
print("\n=== Ejercicio 4: Experiencia total ===")
mision1 = int(input("Ingrese la experiencia ganada en la misión 1: "))
mision2 = int(input("Ingrese la experiencia ganada en la misión 2: "))
mision3 = int(input("Ingrese la experiencia ganada en la misión 3: "))
experiencia_total = mision1 + mision2 + mision3
print("Experiencia total:", experiencia_total)

# --- Ejercicio 5: Porcentaje de vida restante ---
print("\n=== Ejercicio 5: Porcentaje de vida restante ===")
vida_maxima = float(input("Ingrese la vida máxima del personaje: "))
vida_actual = float(input("Ingrese la vida actual del personaje: "))
porcentaje_vida = (vida_actual / vida_maxima) * 100
print("Porcentaje de vida restante:", round(porcentaje_vida, 2), "%")

# --- Ejercicio 6: Oro total recolectado ---
print("\n=== Ejercicio 6: Oro total ===")
oro_mision1 = int(input("Ingrese el oro recolectado en la misión 1: "))
oro_mision2 = int(input("Ingrese el oro recolectado en la misión 2: "))
oro_mision3 = int(input("Ingrese el oro recolectado en la misión 3: "))
oro_total = oro_mision1 + oro_mision2 + oro_mision3
print("Oro total recolectado:", oro_total)

# --- Ejercicio 7: Velocidad promedio de un vehículo ---
print("\n=== Ejercicio 7: Velocidad promedio ===")
distancia = float(input("Ingrese la distancia recorrida (km): "))
tiempo = float(input("Ingrese el tiempo tomado (horas): "))
velocidad_promedio = distancia / tiempo
print("Velocidad promedio:", round(velocidad_promedio, 2), "km/h")

# --- Ejercicio 8: Costo total de mejoras ---
print("\n=== Ejercicio 8: Costo total de mejoras ===")
mejora1 = int(input("Ingrese el costo de la mejora 1: "))
mejora2 = int(input("Ingrese el costo de la mejora 2: "))
mejora3 = int(input("Ingrese el costo de la mejora 3: "))
costo_total = mejora1 + mejora2 + mejora3
print("Costo total de mejoras:", costo_total)

# --- Ejercicio 9: Tiempo restante para completar misión ---
print("\n=== Ejercicio 9: Tiempo restante ===")
tiempo_total_mision = int(input("Ingrese el tiempo total de la misión (segundos): "))
tiempo_transcurrido = int(input("Ingrese el tiempo transcurrido (segundos): "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print("Tiempo restante:", tiempo_restante, "segundos")

# --- Ejercicio 10: Nivel promedio de un equipo ---
print("\n=== Ejercicio 10: Nivel promedio del equipo ===")
nivel_jugador1 = int(input("Ingrese el nivel del jugador 1: "))
nivel_jugador2 = int(input("Ingrese el nivel del jugador 2: "))
nivel_jugador3 = int(input("Ingrese el nivel del jugador 3: "))
nivel_promedio = (nivel_jugador1 + nivel_jugador2 + nivel_jugador3) / 3
print("Nivel promedio del equipo:", round(nivel_promedio, 2))

# --- Ejercicio 11: Daño crítico en un ataque ---
print("\n=== Ejercicio 11: Daño crítico ===")
danio_base = float(input("Ingrese el daño base del ataque: "))
multiplicador_critico = float(input("Ingrese el multiplicador crítico: "))
danio_critico = danio_base * multiplicador_critico
print("Daño crítico:", danio_critico)

# --- Ejercicio 12: Tiempo total en horas y minutos ---
print("\n=== Ejercicio 12: Tiempo en horas y minutos ===")
tiempo_minutos = int(input("Ingrese el tiempo total jugado en minutos: "))
horas_jugadas = tiempo_minutos // 60
minutos_restantes = tiempo_minutos % 60
print("Tiempo jugado:", horas_jugadas, "horas y", minutos_restantes, "minutos")

# --- Ejercicio 13: Porcentaje de misiones completadas ---
print("\n=== Ejercicio 13: Porcentaje de misiones completadas ===")
total_misiones = int(input("Ingrese el número total de misiones: "))
misiones_completadas = int(input("Ingrese el número de misiones completadas: "))
porcentaje_misiones = (misiones_completadas / total_misiones) * 100
print("Porcentaje completado:", round(porcentaje_misiones, 2), "%")

# --- Ejercicio 14: Costo total de objetos en tienda ---
print("\n=== Ejercicio 14: Costo total de objetos ===")
objeto1 = int(input("Ingrese el costo del objeto 1: "))
objeto2 = int(input("Ingrese el costo del objeto 2: "))
objeto3 = int(input("Ingrese el costo del objeto 3: "))
costo_total_objetos = objeto1 + objeto2 + objeto3
print("Costo total de objetos:", costo_total_objetos)

# --- Ejercicio 15: Tiempo promedio de una partida ---
print("\n=== Ejercicio 15: Tiempo promedio de partida ===")
partida1 = float(input("Ingrese el tiempo de la partida 1 (minutos): "))
partida2 = float(input("Ingrese el tiempo de la partida 2 (minutos): "))
partida3 = float(input("Ingrese el tiempo de la partida 3 (minutos): "))
tiempo_promedio = (partida1 + partida2 + partida3) / 3
print("Tiempo promedio de partida:", round(tiempo_promedio, 2), "minutos")

# --- Ejercicio 16: Porcentaje de enemigos derrotados ---
print("\n=== Ejercicio 16: Porcentaje de enemigos derrotados ===")
total_enemigos = int(input("Ingrese el número total de enemigos: "))
enemigos_derrotados = int(input("Ingrese el número de enemigos derrotados: "))
porcentaje_enemigos = (enemigos_derrotados / total_enemigos) * 100
print("Porcentaje de enemigos derrotados:", round(porcentaje_enemigos, 2), "%")