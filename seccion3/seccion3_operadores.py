# =============================================================
# SECCIÓN 3 - Operadores: herramientas de manipulación de datos
# Fundamentos de Python - GA1-220501093-04-AA1-EV01
# =============================================================

# -------------------------------------------------------------
# 1. EXPONENCIACIÓN  (**)
# -------------------------------------------------------------

print("--- Exponenciación ---")
print(2 ** 3)         # int ** int   = int   --> 8
print(2 ** 3.)        # int ** float = float --> 8.0
print(2. ** 3)        # float ** int = float --> 8.0
print(2. ** 3.)       # float ** float = float --> 8.0

# -------------------------------------------------------------
# 2. MULTIPLICACIÓN  (*)
# -------------------------------------------------------------

print("--- Multiplicación ---")
print(2 * 3)          # 6
print(2 * 3.)         # 6.0
print(2. * 3)         # 6.0
print(2. * 3.)        # 6.0

# -------------------------------------------------------------
# 3. DIVISIÓN  (/) - siempre retorna flotante
# -------------------------------------------------------------

print("--- División ---")
print(6 / 3)          # 2.0
print(6 / 3.)         # 2.0
print(6. / 3)         # 2.0
print(6. / 3.)        # 2.0

# -------------------------------------------------------------
# 4. DIVISIÓN ENTERA  (//) - redondea hacia abajo
# -------------------------------------------------------------

print("--- División entera ---")
print(6 // 3)         # 2
print(6 // 3.)        # 2.0
print(6. // 3)        # 2.0
print(6. // 3.)       # 2.0
print(6 // 4)         # 1    (1.5 redondeado hacia abajo)
print(6. // 4)        # 1.0
print(-6 // 4)        # -2   (-1.5 redondeado hacia abajo = -2)
print(6. // -4)       # -2.0

# -------------------------------------------------------------
# 5. MÓDULO / RESIDUO  (%)
# -------------------------------------------------------------

print("--- Módulo ---")
print(14 % 4)         # 2   (14 = 3*4 + 2)
print(12 % 4.5)       # 3.0

# -------------------------------------------------------------
# 6. SUMA  (+)
# -------------------------------------------------------------

print("--- Suma ---")
print(-4 + 4)         # 0
print(-4. + 8)        # 4.0

# -------------------------------------------------------------
# 7. RESTA  (-) - también opera como operador unario
# -------------------------------------------------------------

print("--- Resta ---")
print(-4 - 4)         # -8
print(4. - 8)         # -4.0
print(-1.1)           # -1.1

# Operador unario positivo
print(+2)             # 2

# -------------------------------------------------------------
# 8. PRIORIDAD DE OPERADORES
# ** > unario +/- > * / // % > binario + -
# -------------------------------------------------------------

print("--- Prioridad ---")
print(2 + 3 * 5)          # 17  (primero * luego +)
print((2 + 3) * 5)        # 25  (paréntesis primero)
print(2 ** 2 ** 3)        # 256 (** enlaza derecha a izquierda)
print(9 % 6 % 2)          # 1   (% enlaza izquierda a derecha)
print(-3 ** 2)             # -9  (** antes que unario -)
print(-(3 ** 2))           # -9

# Expresión compleja con paréntesis
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)   # 17.0


# =============================================================
# LAB - Ejercicios de Operadores Matemáticos
# =============================================================
#
# Escenario:
# Cada ejercicio fue resuelto de forma manual y luego comprobado con Python.
# Las soluciones detalladas paso a paso están en operadores.md
# -------------------------------------------------------------

print("\n--- Comprobación de los 15 ejercicios ---")

print("Ej1:", 5 + 3 * 2)                    # 11
print("Ej2:", 8 / 2 + 4 * 3)               # 16.0
print("Ej3:", (7 + 3) * 2 - 5)             # 15
print("Ej4:", 10 - 4 + 2 * 3)              # 12
print("Ej5:", (10 / 2) * (3 + 2) - 4)      # 21.0
print("Ej6:", 2 + 3 * (4 - 1))             # 11
print("Ej7:", 5 * 2 ** 3)                  # 40
print("Ej8:", 6 + 4 / 2 ** 2)              # 7.0
print("Ej9:", 10 % 3 + 2 * 5)              # 11
print("Ej10:", (8 + 2) * 3 ** 2)           # 90
print("Ej11:", 7 + 2 * (3 + 5) / 4)        # 11.0
print("Ej12:", 2 ** 3 * 4 / 2)             # 16.0
print("Ej13:", 9 - 6 + 3 ** 2)             # 12
print("Ej14:", (7 - 2) * 5 + 3 ** 2)       # 34
print("Ej15:", 4 * 2 ** 3 / 8 + 1)         # 5.0