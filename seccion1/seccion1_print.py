# =============================================================
# SECCIÓN 1 - El Programa "¡Hola, Mundo!" y la función print()
# Fundamentos de Python - GA1-220501093-04-AA1-EV01
# =============================================================

# -------------------------------------------------------------
# 1. TU PRIMER PROGRAMA
# -------------------------------------------------------------
print("¡Hola, Mundo!")

# -------------------------------------------------------------
# 2. LA FUNCIÓN print() - efecto, argumentos y valor retornado
# -------------------------------------------------------------

# print() envía datos al dispositivo de salida (consola)
print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

# print() vacío genera una línea en blanco
print("La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")

# -------------------------------------------------------------
# 3. CARACTERES DE ESCAPE Y NUEVA LÍNEA  (\n)
# -------------------------------------------------------------

# \n dentro de una cadena produce un salto de línea
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")

# Para imprimir una sola barra invertida se duplica: \\
print("Barra invertida: \\")

# -------------------------------------------------------------
# 4. USANDO MÚLTIPLES ARGUMENTOS
# -------------------------------------------------------------

# Los argumentos se separan con coma; print() añade un espacio entre ellos
print("La Witsi Witsi Araña", "subió", "a su telaraña.")

# -------------------------------------------------------------
# 5. ARGUMENTOS POSICIONALES
# -------------------------------------------------------------

print("Mi nombre es", "Python.")
print("Monty Python.")

# -------------------------------------------------------------
# 6. ARGUMENTOS DE PALABRA CLAVE: end y sep
# -------------------------------------------------------------

# end: define qué se imprime al final (por defecto es \n)
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# end vacío: no genera salto de línea al final
print("Mi nombre es ", end="")
print("Monty Python.")

# sep: define el separador entre argumentos (por defecto es espacio)
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

# Combinando sep y end
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


# =============================================================
# LAB 1 - Trabajando con la función print()
# =============================================================
#
# Escenario:
# Utiliza la función print() para imprimir ¡Hola, Mundo! en pantalla.
# Usa comillas dobles alrededor de la cadena.
# Luego imprime tu nombre.
# Experimenta quitando comillas, quitando paréntesis y usando comillas simples.
#
# ¿Qué error arroja al quitar las comillas?
#   --> SyntaxError: invalid syntax
#       Python interpreta el texto como código, no como cadena.
#
# ¿Qué error arroja al quitar los paréntesis?
#   --> SyntaxError: Missing parentheses in call to 'print'
#       En Python 3 print es función y SIEMPRE necesita paréntesis.
# -------------------------------------------------------------

# Parte 1: Hola Mundo con comillas dobles
print("¡Hola, Mundo!")

# Parte 2: Imprimir nombre
print("Sara Garcia")

# Parte 3: Error sin comillas (comentado - no ejecutar)
# print(¡Hola, Mundo!)   --> SyntaxError: invalid syntax

# Parte 4: Error sin paréntesis (comentado - no ejecutar)
# print "¡Hola, Mundo!"  --> SyntaxError: Missing parentheses in call to 'print'

# Parte 5: Usando comillas simples
print('¡Hola, Mundo!')
print('Sara Garcia')

# Parte 6: Múltiples print() en líneas diferentes
print("Línea 1")
print("Línea 2")
print("Línea 3")

# Parte 7: Múltiples argumentos en un solo print()
print("Hola", "Mundo", "desde", "Python")

# Parte 8: print() vacío genera línea en blanco
print("Antes de la línea en blanco")
print()
print("Después de la línea en blanco")


# =============================================================
# LAB 2 - La función print() y sus argumentos
# =============================================================
#
# Escenario:
# Practica el uso de sep y end para controlar el formato de salida.
# -------------------------------------------------------------

print("La Witsi Witsi Araña", "subió", "a su telaraña.")
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


# =============================================================
# LAB 3 - Dando formato a la salida
# =============================================================
#
# Escenario:
# Combina sep, end y \n para producir distintos formatos de salida.
# -------------------------------------------------------------

# Separador vacío
print("Hola", "Mundo", sep="")

# Separador con símbolo
print("Python", "es", "genial", sep=" | ")

# Sin salto de línea al final
print("Cargando", end="")
print(".", end="")
print(".", end="")
print(".", end="\n")

# Usando \n dentro de una cadena
print("Línea 1\nLínea 2\nLínea 3")