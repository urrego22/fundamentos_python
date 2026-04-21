<div align="center">

# 🐍 Fundamentos de Python

### `GA1-220501093-04-AA1-EV01`

> Proyecto educativo que abarca los fundamentos esenciales de Python: desde la función `print()` hasta el manejo de variables, literales, operadores aritméticos y entrada de datos por consola.

</div>

---

## 👩‍💻 Desarrolladora

| Campo | Detalle |
|-------|---------|
| **Nombre** | Sara Garcia |
| **Programa** | Análisis y Desarrollo de Software — SENA |
| **Actividad** | GA1-220501093-04-AA1-EV01 |

---

## 📁 Estructura del Repositorio

```
fundamentos_python/
│
├── 📂 seccion1/
│   └── seccion1_print.py          # Función print(), escape y argumentos
│
├── 📂 seccion2/
│   └── seccion2_literales.py      # Tipos de literales en Python
│
├── 📂 seccion3/
│   ├── seccion3_operadores.py     # Operadores matemáticos
│   └── operadores.md              # Soluciones detalladas con explicación
│
├── 📂 seccion4/
│   └── seccion4_variables.py      # Variables, operadores abreviados y 16 algoritmos
│
├── 📂 src/
│   └── puntaje_final_jugador.py   # Proyecto final integrador
│
└── README.md
```

---

## ▶️ Cómo Ejecutar los Programas

### Requisitos previos
- Tener **Python 3** instalado → [Descargar aquí](https://www.python.org/downloads/)
- Abrir la terminal en la **carpeta raíz** del proyecto

### Comandos de ejecución

```bash
# Sección 1 - print()
python seccion1/seccion1_print.py

# Sección 2 - Literales
python seccion2/seccion2_literales.py

# Sección 3 - Operadores
python seccion3/seccion3_operadores.py

# Sección 4 - Variables y algoritmos (requiere entrada de datos)
python seccion4/seccion4_variables.py

# Proyecto final
python src/puntaje_final_jugador.py
```

> ⚠️ La **Sección 4 - LAB 4** solicita datos al usuario por consola mediante `input()`. Ten listos los valores antes de ejecutar.

---

## 📚 Contenido por Secciones

---

### 🖨️ Sección 1 — La función `print()` y el primer programa

La función `print()` es el punto de partida en Python. Permite mostrar información en la consola y es esencial para comunicar resultados al usuario.

**Temas cubiertos:**

| Tema | Descripción |
|------|-------------|
| `print()` básico | Imprime texto en consola |
| Caracteres de escape `\n` | Salto de línea dentro de una cadena |
| Múltiples argumentos | Se pueden pasar varios valores separados por coma |
| Argumento `sep` | Define el separador entre argumentos (por defecto es un espacio) |
| Argumento `end` | Define qué se imprime al final (por defecto es `\n`) |

<details>
<summary>📖 Ver laboratorios de la Sección 1</summary>

---

#### 🧪 LAB 1 — Trabajando con la función `print()`

**Objetivo:** Imprimir `¡Hola, Mundo!` y el nombre del desarrollador. Experimentar con errores comunes.

**Errores explorados:**

```python
# ❌ Sin comillas → SyntaxError
print(Hola Mundo)

# ❌ Sin paréntesis → SyntaxError en Python 3
print "Hola Mundo"

# ✅ Correcto
print("¡Hola, Mundo!")
```

> 💡 En Python 3, `print` es una **función** y siempre requiere paréntesis. En Python 2 era una sentencia, por eso el error es diferente.

---

#### 🧪 LAB 2 — La función `print()` y sus argumentos

**Objetivo:** Controlar el formato de salida con `sep` y `end`.

```python
# sep cambia el separador entre valores
print("Python", "es", "genial", sep="-")
# Salida: Python-es-genial

# end evita el salto de línea automático
print("Hola", end=" ")
print("Mundo")
# Salida: Hola Mundo
```

---

#### 🧪 LAB 3 — Dando formato a la salida

**Objetivo:** Combinar `sep`, `end` y `\n` para producir distintos formatos de salida de forma creativa.

```python
print("*", "*", "*", sep="\n", end="\n---\n")
```

---

</details>

---

### 🔢 Sección 2 — Literales de Python

Un **literal** es un valor fijo escrito directamente en el código. Python soporta varios tipos de literales que representan distintos tipos de datos.

**Temas cubiertos:**

| Tipo de Literal | Ejemplo | Descripción |
|-----------------|---------|-------------|
| Entero decimal | `42` | Número entero estándar |
| Entero octal | `0o52` | Base 8, prefijo `0o` |
| Entero hexadecimal | `0x2A` | Base 16, prefijo `0x` |
| Flotante | `3.14` | Número con decimal |
| Notación científica | `3.14e2` → `314.0` | Potencias de 10 |
| Cadena (string) | `"texto"` o `'texto'` | Texto entre comillas |
| Booleano | `True` / `False` | Valor lógico |

<details>
<summary>📖 Ver laboratorio de la Sección 2</summary>

---

#### 🧪 LAB — Literales de Python: Cadenas y caracteres de escape

**Objetivo:** Escribir **una sola instrucción** `print()` que produzca exactamente esta salida:

```
"Estoy"
""aprendiendo""
"""Python"""
```

**Solución:**
```python
print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")
```

**¿Por qué funciona?**

| Escape | Resultado |
|--------|-----------|
| `\"` | Comilla doble literal dentro de una cadena |
| `\n` | Salto de línea |

> 💡 Las comillas de escape `\"` permiten incluir el carácter `"` dentro de una cadena delimitada con `"`, sin cerrarla accidentalmente.

---

</details>

---

### ➗ Sección 3 — Operadores Matemáticos

Python respeta la **jerarquía estándar de operadores** matemáticos (PEMDAS). Entender el orden de evaluación es fundamental para escribir expresiones correctas.

**Operadores disponibles:**

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `**` | Potenciación | `2 ** 3` | `8` |
| `*` | Multiplicación | `4 * 5` | `20` |
| `/` | División real | `7 / 2` | `3.5` |
| `//` | División entera | `7 // 2` | `3` |
| `%` | Módulo (resto) | `7 % 2` | `1` |
| `+` | Suma | `3 + 4` | `7` |
| `-` | Resta | `9 - 5` | `4` |

> ⚠️ La `/` **siempre** retorna un `float`, incluso si el resultado es exacto: `4 / 2 = 2.0`  
> ⚠️ La `//` redondea **hacia abajo** (floor), incluso en negativos: `-7 // 2 = -4`

**Prioridad de operadores (de mayor a menor):**
```
1. ()            → Paréntesis
2. **            → Potenciación (asociatividad derecha)
3. *, /, //, %   → Multiplicación y división
4. +, -          → Suma y resta
```

<details>
<summary>📖 Ver tabla completa de ejercicios resueltos</summary>

---

#### 🧪 LAB — 15 Ejercicios de Operadores Matemáticos

Cada ejercicio fue resuelto **manualmente** aplicando las reglas de prioridad y luego verificado con Python.

| # | Expresión | Paso a paso | Resultado |
|---|-----------|-------------|-----------|
| 1 | `5 + 3 * 2` | `5 + 6` | **`11`** |
| 2 | `8 / 2 + 4 * 3` | `4.0 + 12` | **`16.0`** |
| 3 | `(7 + 3) * 2 - 5` | `10 * 2 - 5 = 20 - 5` | **`15`** |
| 4 | `10 - 4 + 2 * 3` | `10 - 4 + 6` | **`12`** |
| 5 | `(10 / 2) * (3 + 2) - 4` | `5.0 * 5 - 4` | **`21.0`** |
| 6 | `2 + 3 * (4 - 1)` | `2 + 3 * 3 = 2 + 9` | **`11`** |
| 7 | `5 * 2 ** 3` | `5 * 8` | **`40`** |
| 8 | `6 + 4 / 2 ** 2` | `6 + 4 / 4 = 6 + 1.0` | **`7.0`** |
| 9 | `10 % 3 + 2 * 5` | `1 + 10` | **`11`** |
| 10 | `(8 + 2) * 3 ** 2` | `10 * 9` | **`90`** |
| 11 | `7 + 2 * (3 + 5) / 4` | `7 + 2 * 8 / 4 = 7 + 4.0` | **`11.0`** |
| 12 | `2 ** 3 * 4 / 2` | `8 * 4 / 2 = 32 / 2` | **`16.0`** |
| 13 | `9 - 6 + 3 ** 2` | `9 - 6 + 9` | **`12`** |
| 14 | `(7 - 2) * 5 + 3 ** 2` | `5 * 5 + 9 = 25 + 9` | **`34`** |
| 15 | `4 * 2 ** 3 / 8 + 1` | `4 * 8 / 8 + 1 = 4.0 + 1` | **`5.0`** |

> 📄 Soluciones detalladas disponibles en [`seccion3/operadores.md`](seccion3/operadores.md)

---

</details>

---

### 📦 Sección 4 — Variables y Operadores Abreviados

Una **variable** es un espacio en memoria que almacena un valor. En Python no se necesita declarar el tipo: Python lo infiere automáticamente según el valor asignado.

**Temas cubiertos:**

#### Creación y reasignación de variables

```python
# Crear variables de distintos tipos
edad = 20
nombre = "Sara"
promedio = 4.5

# Reasignar
edad = 21          # Cambia el valor
edad = edad + 1    # Usa el valor anterior para calcular el nuevo
```

#### Nombres válidos de variables

| ✅ Válido | ❌ Inválido | Razón |
|-----------|------------|-------|
| `vida_maxima` | `vida maxima` | No se permiten espacios |
| `nivel1` | `1nivel` | No puede empezar con número |
| `_puntos` | `for` | No puede ser palabra reservada |
| `danio_total` | `daño-total` | No se permiten guiones ni tildes |

#### Operadores abreviados

Permiten escribir operaciones de actualización de forma más compacta y legible:

| Operador | Equivale a | Ejemplo | Resultado |
|----------|-----------|---------|-----------|
| `x += 5` | `x = x + 5` | `x = 10` → `x += 5` | `15` |
| `x -= 3` | `x = x - 3` | `x = 15` → `x -= 3` | `12` |
| `x *= 2` | `x = x * 2` | `x = 12` → `x *= 2` | `24` |
| `x /= 4` | `x = x / 4` | `x = 24` → `x /= 4` | `6.0` |
| `x //= 2` | `x = x // 2` | `x = 6.0` → `x //= 2` | `3.0` |
| `x **= 3` | `x = x ** 3` | `x = 3.0` → `x **= 3` | `27.0` |
| `x %= 5` | `x = x % 5` | `x = 27.0` → `x %= 5` | `2.0` |

<details>
<summary>📖 Ver laboratorios de la Sección 4</summary>

---

#### 🧪 LAB 1 — Variables básicas

**Objetivo:** Crear variables de distintos tipos, reasignar valores y aplicar el **Teorema de Pitágoras**.

```python
# Teorema de Pitágoras: c = √(a² + b²)
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("Hipotenusa c =", c)
# Salida: Hipotenusa c = 5.0
```

> 💡 `** 0.5` es equivalente a calcular la raíz cuadrada, ya que `√x = x^(1/2)`.

---

#### 🧪 LAB 2 — Convertidor simple (millas ↔ kilómetros)

**Objetivo:** Convertir entre unidades de distancia usando la equivalencia `1 milla = 1.61 km`.

```python
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
```

**Salida esperada:**
```
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
```

> 💡 `round(valor, 2)` redondea el resultado a **2 decimales** para una salida más limpia.

---

#### 🧪 LAB 3 — Operadores y expresiones

**Objetivo:** Evaluar la expresión polinómica `3x³ - 2x² + 3x - 1` para distintos valores de `x`.

```python
# Fórmula: y = 3x³ - 2x² + 3x - 1
x = float(0)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)   # y = -1.0

x = float(1)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)   # y = 3.0

x = float(-1)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)   # y = -9.0
```

**Salida esperada:**
```
y = -1.0
y = 3.0
y = -9.0
```

> 💡 Se usa `float()` para forzar resultados decimales y mantener consistencia de tipo.

---

#### 🧪 LAB 4 — Ejercicios de Algoritmos (Gameplay) 🎮

**Escenario:** Eres un desarrollador de mecánicas de videojuego. Debes implementar 16 algoritmos que calculan estadísticas del juego. Cada uno **solicita los datos al usuario** mediante `input()` y realiza el cálculo correspondiente.

| # | Algoritmo | Datos de entrada | Operación principal |
|---|-----------|-----------------|---------------------|
| 1 | Puntaje total del jugador | Puntos de 3 niveles | Suma |
| 2 | Tiempo total de juego en segundos | Horas, minutos y segundos | Conversión y suma |
| 3 | Daño total de un personaje | Daño de 3 ataques | Suma |
| 4 | Experiencia total ganada | XP de 3 misiones | Suma |
| 5 | Porcentaje de vida restante | Vida máxima y vida actual | `(actual / máx) * 100` |
| 6 | Oro total recolectado | Oro de 3 misiones | Suma |
| 7 | Velocidad promedio de vehículo | Distancia y tiempo | `distancia / tiempo` |
| 8 | Costo total de mejoras | Costo de 3 mejoras | Suma |
| 9 | Tiempo restante de misión | Tiempo total y transcurrido | Resta |
| 10 | Nivel promedio del equipo | Nivel de 3 jugadores | Promedio |
| 11 | Daño crítico en un ataque | Daño base y multiplicador | Multiplicación |
| 12 | Tiempo en horas y minutos | Minutos totales | `//` y `%` |
| 13 | Porcentaje de misiones completadas | Total y completadas | `(comp / total) * 100` |
| 14 | Costo total de objetos en tienda | Costo de 3 objetos | Suma |
| 15 | Tiempo promedio de partida | Duración de 3 partidas | Promedio |
| 16 | Porcentaje de enemigos derrotados | Total y derrotados | `(derrot / total) * 100` |

**Ejemplo de ejecución — Ejercicio 12:**
```
=== Ejercicio 12: Tiempo en horas y minutos ===
Ingrese el tiempo total jugado en minutos: 145
Tiempo jugado: 2 horas y 25 minutos
```

> 💡 El ejercicio 12 usa `//` para obtener las horas enteras y `%` para los minutos restantes:  
> `145 // 60 = 2 horas` | `145 % 60 = 25 minutos`

---

</details>

---

### 🎮 src — Proyecto Final Integrador

**Archivo:** `src/puntaje_final_jugador.py`

Programa completo que integra todos los conceptos trabajados en las cuatro secciones:

- ✅ Uso de `print()` con formato
- ✅ Tipos de datos y literales
- ✅ Operadores aritméticos
- ✅ Variables y operadores abreviados
- ✅ Entrada de datos con `input()`
- ✅ Manejo y presentación de cadenas

---

## ✅ Conclusiones

A lo largo de este proyecto se consolidaron los siguientes conceptos fundamentales de Python:

| Concepto | Aprendizaje clave |
|----------|------------------|
| `print()` | Es una función en Python 3 y siempre requiere paréntesis |
| Literales | Python soporta enteros, flotantes, cadenas, booleanos y notación científica |
| Operadores | Python respeta la jerarquía matemática estándar (potencia > mult/div > suma/resta) |
| División `/` | Siempre retorna `float`, incluso si el resultado es exacto |
| División `//` | Redondea hacia abajo (**floor**), incluso en números negativos |
| Módulo `%` | Útil para verificar paridad, distribuir elementos o convertir unidades de tiempo |
| Paréntesis | Permiten controlar y sobrescribir el orden de evaluación |
| Variables | No requieren declaración de tipo; Python lo infiere automáticamente |
| Operadores abreviados | `+=`, `-=`, `*=`, etc. hacen el código más compacto y legible |
| `input()` | Permite capturar datos del usuario en tiempo de ejecución (siempre retorna `str`) |

---

<div align="center">

**Desarrollado por Sara Garcia**  
Análisis y Desarrollo de Software — SENA  
`GA1-220501093-04-AA1-EV01`

</div>