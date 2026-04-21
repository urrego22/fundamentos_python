# =============================================================
# SECCIÓN 2 - Literales de Python
# Fundamentos de Python - GA1-220501093-04-AA1-EV01
# =============================================================

# -------------------------------------------------------------
# 1. LITERALES ENTEROS
# -------------------------------------------------------------

print(123)
print(-456)
print(11111111)
print(11_111_111)     # guion bajo como separador visual (Python 3.6+)

# Octal: prefijo 0o
print(0o123)          # octal --> 83 en decimal

# Hexadecimal: prefijo 0x
print(0x123)          # hex   --> 291 en decimal

# -------------------------------------------------------------
# 2. LITERALES FLOTANTES
# -------------------------------------------------------------

print(2.5)
print(-0.4)
print(0.4)
print(.4)             # el cero antes del punto es opcional
print(4.)             # el cero después del punto es opcional

# Notación científica con E
print(3E8)            # 3 x 10^8 = 300000000.0  (velocidad de la luz)
print(6.62607E-34)    # constante de Planck
print(0.0000000000000000000001)   # Python lo muestra como 1e-22

# Entero vs Flotante
print(4)              # entero
print(4.0)            # flotante

# -------------------------------------------------------------
# 3. CADENAS
# -------------------------------------------------------------

print("Yo soy una cadena.")
print('Yo también soy una cadena.')

# Comilla doble dentro de cadena con escape
print("Me gusta \"Monty Python\"")

# Comilla doble dentro de cadena usando apóstrofes
print('Me gusta "Monty Python"')

# Apóstrofe dentro de cadena con escape
print('I\'m Monty Python.')

# -------------------------------------------------------------
# 4. VALORES BOOLEANOS
# -------------------------------------------------------------

print(True)
print(False)
print(True > False)   # True  (1 > 0)
print(True < False)   # False (1 < 0)


# =============================================================
# LAB - Literales de Python: Cadenas
# =============================================================
#
# Escenario:
# Escriba un fragmento de código de UNA SOLA LÍNEA usando print(),
# caracteres de nuevalínea (\n) y de escape (\") para producir
# exactamente la siguiente salida:
#
# Salida Esperada:
# "Estoy"
# ""aprendiendo""
# """Python"""
#
# Explicación:
# \"   --> imprime una comilla doble "
# \n   --> inserta un salto de línea
# -------------------------------------------------------------

print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")