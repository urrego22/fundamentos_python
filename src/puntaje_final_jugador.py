# Proyecto: Puntaje Final del Jugador
# Integra: variables, operadores y cadenas

nombre_jugador = "Ana"
puntaje_nivel1 = 850
puntaje_nivel2 = 920
puntaje_nivel3 = 760
bonus = 500

# Calcular puntaje total con bonus
puntaje_total = puntaje_nivel1 + puntaje_nivel2 + puntaje_nivel3 + bonus

# Calcular promedio por nivel
promedio = (puntaje_nivel1 + puntaje_nivel2 + puntaje_nivel3) / 3

# Determinar rango usando operadores
puntaje_maximo_posible = 3000
porcentaje = (puntaje_total - bonus) / puntaje_maximo_posible * 100

print("===== RESULTADO FINAL DEL JUGADOR =====")
print("Jugador:", nombre_jugador)
print("Puntaje Nivel 1:", puntaje_nivel1)
print("Puntaje Nivel 2:", puntaje_nivel2)
print("Puntaje Nivel 3:", puntaje_nivel3)
print("Bonus:", bonus)
print("----------------------------------------")
print("Puntaje Total:", puntaje_total)
print("Promedio por nivel:", promedio)
print("Porcentaje de efectividad:", porcentaje, "%")
print("========================================")