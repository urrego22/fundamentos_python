# Ejercicios de Operadores Matematicos
### Seccion 3 - Fundamentos de Python

Basado en los conceptos anteriormente trabajados, el aprendiz resolvió de forma
manual los ejercicios y luego los comprobó con Python.
El formato sigue el modelo del Ejercicio 1.

---

## Ejercicio 1

Expresión: `5 + 3 * 2`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
5 + 3 * 2
```

Paso a paso:

1. Identificar las operaciones y su prioridad:
   - Suma (`+`)
   - Multiplicación (`*`)
   - La multiplicación tiene mayor prioridad que la suma.
2. Realizar la multiplicación primero:
   - `3 * 2 = 6`
3. Realizar la suma:
   - `5 + 6 = 11`

Resultado final:

```python
11
```

Comprobación en Python:
```python
print(5 + 3 * 2)  # 11
```

---

## Ejercicio 2

Expresión: `8 / 2 + 4 * 3`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
8 / 2 + 4 * 3
```

Paso a paso:

1. División (`/`) y multiplicación (`*`) tienen la misma prioridad; de izquierda a derecha.
2. `8 / 2 = 4.0`
3. `4 * 3 = 12`
4. `4.0 + 12 = 16.0`

Resultado final:

```python
16.0
```

Comprobación en Python:
```python
print(8 / 2 + 4 * 3)  # 16.0
```

---

## Ejercicio 3

Expresión: `(7 + 3) * 2 - 5`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
(7 + 3) * 2 - 5
```

Paso a paso:

1. Paréntesis primero: `7 + 3 = 10`
2. Multiplicación: `10 * 2 = 20`
3. Resta: `20 - 5 = 15`

Resultado final:

```python
15
```

Comprobación en Python:
```python
print((7 + 3) * 2 - 5)  # 15
```

---

## Ejercicio 4

Expresión: `10 - 4 + 2 * 3`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
10 - 4 + 2 * 3
```

Paso a paso:

1. Multiplicación primero: `2 * 3 = 6`
2. Resta y suma de izquierda a derecha: `10 - 4 = 6`, `6 + 6 = 12`

Resultado final:

```python
12
```

Comprobación en Python:
```python
print(10 - 4 + 2 * 3)  # 12
```

---

## Ejercicio 5

Expresión: `(10 / 2) * (3 + 2) - 4`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
(10 / 2) * (3 + 2) - 4
```

Paso a paso:

1. Primer paréntesis: `10 / 2 = 5.0`
2. Segundo paréntesis: `3 + 2 = 5`
3. Multiplicación: `5.0 * 5 = 25.0`
4. Resta: `25.0 - 4 = 21.0`

Resultado final:

```python
21.0
```

Comprobación en Python:
```python
print((10 / 2) * (3 + 2) - 4)  # 21.0
```

---

## Ejercicio 6

Expresión: `2 + 3 * (4 - 1)`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
2 + 3 * (4 - 1)
```

Paso a paso:

1. Paréntesis: `4 - 1 = 3`
2. Multiplicación: `3 * 3 = 9`
3. Suma: `2 + 9 = 11`

Resultado final:

```python
11
```

Comprobación en Python:
```python
print(2 + 3 * (4 - 1))  # 11
```

---

## Ejercicio 7

Expresión: `5 * 2 ** 3`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
5 * 2 ** 3
```

Paso a paso:

1. Exponenciación (prioridad más alta): `2 ** 3 = 8`
2. Multiplicación: `5 * 8 = 40`

Resultado final:

```python
40
```

Comprobación en Python:
```python
print(5 * 2 ** 3)  # 40
```

---

## Ejercicio 8

Expresión: `6 + 4 / 2 ** 2`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
6 + 4 / 2 ** 2
```

Paso a paso:

1. Exponenciación: `2 ** 2 = 4`
2. División: `4 / 4 = 1.0`
3. Suma: `6 + 1.0 = 7.0`

Resultado final:

```python
7.0
```

Comprobación en Python:
```python
print(6 + 4 / 2 ** 2)  # 7.0
```

---

## Ejercicio 9

Expresión: `10 % 3 + 2 * 5`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
10 % 3 + 2 * 5
```

Paso a paso:

1. Módulo y multiplicación misma prioridad; de izquierda a derecha.
2. `10 % 3 = 1` (cociente 3, residuo 1)
3. `2 * 5 = 10`
4. `1 + 10 = 11`

Resultado final:

```python
11
```

Comprobación en Python:
```python
print(10 % 3 + 2 * 5)  # 11
```

---

## Ejercicio 10

Expresión: `(8 + 2) * 3 ** 2`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
(8 + 2) * 3 ** 2
```

Paso a paso:

1. Paréntesis: `8 + 2 = 10`
2. Exponenciación: `3 ** 2 = 9`
3. Multiplicación: `10 * 9 = 90`

Resultado final:

```python
90
```

Comprobación en Python:
```python
print((8 + 2) * 3 ** 2)  # 90
```

---

## Ejercicio 11

Expresión: `7 + 2 * (3 + 5) / 4`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
7 + 2 * (3 + 5) / 4
```

Paso a paso:

1. Paréntesis: `3 + 5 = 8`
2. Multiplicación y división de izquierda a derecha: `2 * 8 = 16`, `16 / 4 = 4.0`
3. Suma: `7 + 4.0 = 11.0`

Resultado final:

```python
11.0
```

Comprobación en Python:
```python
print(7 + 2 * (3 + 5) / 4)  # 11.0
```

---

## Ejercicio 12

Expresión: `2 ** 3 * 4 / 2`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
2 ** 3 * 4 / 2
```

Paso a paso:

1. Exponenciación: `2 ** 3 = 8`
2. Multiplicación y división de izquierda a derecha: `8 * 4 = 32`, `32 / 2 = 16.0`

Resultado final:

```python
16.0
```

Comprobación en Python:
```python
print(2 ** 3 * 4 / 2)  # 16.0
```

---

## Ejercicio 13

Expresión: `9 - 6 + 3 ** 2`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
9 - 6 + 3 ** 2
```

Paso a paso:

1. Exponenciación: `3 ** 2 = 9`
2. Resta y suma de izquierda a derecha: `9 - 6 = 3`, `3 + 9 = 12`

Resultado final:

```python
12
```

Comprobación en Python:
```python
print(9 - 6 + 3 ** 2)  # 12
```

---

## Ejercicio 14

Expresión: `(7 - 2) * 5 + 3 ** 2`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
(7 - 2) * 5 + 3 ** 2
```

Paso a paso:

1. Paréntesis: `7 - 2 = 5`
2. Exponenciación: `3 ** 2 = 9`
3. Multiplicación: `5 * 5 = 25`
4. Suma: `25 + 9 = 34`

Resultado final:

```python
34
```

Comprobación en Python:
```python
print((7 - 2) * 5 + 3 ** 2)  # 34
```

---

## Ejercicio 15

Expresión: `4 * 2 ** 3 / 8 + 1`

- Pregunta: ¿Cuál es el resultado? ¿Por qué?

**Solución y Explicación**

```python
4 * 2 ** 3 / 8 + 1
```

Paso a paso:

1. Exponenciación: `2 ** 3 = 8`
2. Multiplicación y división de izquierda a derecha: `4 * 8 = 32`, `32 / 8 = 4.0`
3. Suma: `4.0 + 1 = 5.0`

Resultado final:

```python
5.0
```

Comprobación en Python:
```python
print(4 * 2 ** 3 / 8 + 1)  # 5.0
```

---

## Resumen de reglas de prioridad

| Prioridad | Operador     | Nombre          |
|-----------|--------------|-----------------|
| 1 (mayor) | `()`         | Paréntesis      |
| 2         | `**`         | Exponenciación  |
| 3         | `* / // %`   | Mult y División |
| 4 (menor) | `+ -`        | Suma y Resta    |

- Misma prioridad → se evalúan de **izquierda a derecha**.
- Excepción: `**` se evalúa de **derecha a izquierda**.