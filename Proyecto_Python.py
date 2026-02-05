"""1. Se crea una cadena de texto y se devuelve un diccionario con las
    frecuencias de cada letra en la cadena. Los espacios no se consideran.

    Devuelve un diccionario donde las claves son las letras y los valores el número de veces que aparecen.

    Parámetros: La cadena de texto sobre la que se calculará la frecuencia de letras.

    Retorna: Diccionario con las letras como claves y sus frecuencias como valores.

    conteo_frecuencia("cadena") {'c': 1, 'a': 2, 'd': 1, 'e': 1, 'n': 1}
    """

def conteo_frecuencia(cadena):

    # Creamos un diccionario vacío donde guardaremos la frecuencia de cada letra
    frecuencias = {}

    # Recorremos cada letra de la cadena
    for letra in cadena:
        # Ignoramos los espacios, no se cuentan
        if letra == " ":
            continue

        # Si la letra ya está en el diccionario, sumamos 1 a su contador
        if letra in frecuencias:
            frecuencias[letra] += 1
        # Si la letra no está en el diccionario, la agregamos con valor 1
        else:
            frecuencias[letra] = 1

    # Mostramos el diccionario resultante
    print(frecuencias)

    # Devolvemos el diccionario con las frecuencias
    return frecuencias

# Ejemplo de uso de la función
conteo_frecuencia("cadena")  # Salida: {'c': 1, 'a': 2, 'd': 1, 'e': 1, 'n': 1}


"""2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()"""

# Lista de ventas diarias (en miles de dólares)
ventas_diarias = [120, 85, 90, 100, 75]  

# Usamos map() para crear una nueva lista donde cada valor se multiplica por 2
# lambda x: x * 2 es una función anónima que toma cada elemento x y lo duplica
ventas_proyectadas = list(map(lambda x: x * 2, ventas_diarias))

# Mostramos la lista original de ventas
print("Ventas originales:", ventas_diarias)

# Mostramos la nueva lista con las ventas proyectadas (cada valor duplicado)
print("Ventas proyectadas (doble):", ventas_proyectadas)


"""3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""

clientes = [
    "TechCorp",
    "GreenFoods",
    "HealthCorp",
    "FastDelivery",
    "EcoCorp",
    "SuperMarket"
]

palabra_objetivo = "Corp"

# Función para filtrar
def filtrar_clientes(lista, objetivo):
    resultado = []
    for nombre in lista:
        if objetivo in nombre:  # verifica si 'Corp' está en el nombre
            resultado.append(nombre)
    return resultado

clientes_filtrados = filtrar_clientes(clientes, palabra_objetivo)
print(clientes_filtrados)

"""4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""

ventas_proyectadas = [120, 85, 90, 100, 75]  # en miles de dólares
ventas_reales     = [115, 90, 88, 105, 70]  # en miles de dólares
def diferencia_listas(lista1, lista2):
    """
    Devuelve una lista con la diferencia entre cada elemento de lista2 y lista1
    """
    return list(map(lambda x, y: y - x, lista1, lista2))
diferencias = diferencia_listas(ventas_proyectadas, ventas_reales)
print(diferencias)


"""5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado."""

def calcular_media_estado(numeros, nota_aprobado=5):
    """
    Calcula la media de una lista de números y devuelve una tupla con:
    (media, estado), donde estado es "aprobado" si la media >= nota_aprobado,
    o "suspenso" si la media < nota_aprobado.
    """
    if not numeros: 
        return (0, "suspenso")
    
    media = sum(numeros) / len(numeros) 
    
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (media, estado)

ventas_equipo = [4.5, 6.2, 5.0, 4.8, 5.5]
media, estado = calcular_media_estado(ventas_equipo, nota_aprobado=5)

print(f"Media de ventas: {media:.2f}k, Estado: {estado}")



"""6. Escribe una función que calcule el factorial de un número de manera recursiva.
"""

# Definimos una función que calcula el factorial de un número de forma recursiva
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Caso recursivo: n! = n * (n-1)!
        return n * factorial(n - 1)

variables = 5

total_combinaciones = factorial(variables)

print(total_combinaciones)


"""7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
"""

datos = [
    ("Ventas", 5200),
    ("Costes", 3100),
    ("Beneficio", 2100)
]

# Función que convierte una lista de tuplas a una lista de strings
def tuplas_a_strings(lista_tuplas):
    # Usamos map() para transformar cada tupla en un string con formato "clave: valor"
    # t[0] es el primer elemento de la tupla (por ejemplo, "Ventas")
    # t[1] es el segundo elemento de la tupla (por ejemplo, 5200)
    return list(map(lambda t: f"{t[0]}: {t[1]}", lista_tuplas))

resultado = tuplas_a_strings(datos)

print(resultado)



"""8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.
"""

# Bloque try: intentamos ejecutar las operaciones que pueden generar errores
try:
    # Solicitamos al usuario el primer número y lo convertimos a float
    num1 = float(input("Introduce el primer número: "))
    
    # Solicitamos al usuario el segundo número y lo convertimos a float
    num2 = float(input("Introduce el segundo número: "))
    
    # Intentamos realizar la división
    resultado = num1 / num2
    
    # Si no hay errores, mostramos el resultado
    print(f"La división fue exitosa. Resultado: {resultado}")

# Capturamos la excepción si el usuario ingresa un valor no numérico
except ValueError:
    print("Error: debes introducir valores numéricos.")

# Capturamos la excepción si se intenta dividir entre cero
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")

# El bloque else se ejecuta si no se produjo ninguna excepción
else:
    print("Operación realizada correctamente.")

# El bloque finally se ejecuta siempre, haya habido excepción o no
finally:
    print("Programa finalizado.")


"""9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
"""

# Función que filtra mascotas prohibidas en España
def filtrar_mascotas_prohibidas(lista_mascotas):
    # Lista de mascotas que no están permitidas
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    # Usamos filter() para crear un nuevo iterable con mascotas permitidas
    # lambda verifica que cada mascota NO esté en la lista de prohibidas
    # Convertimos el resultado de filter a lista con list()
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

mascotas = [
    "Perro",
    "Gato",
    "Mapache",
    "Loro",
    "Serpiente Pitón",
    "Hamster"
]

resultado = filtrar_mascotas_prohibidas(mascotas)

print(resultado)

""" 10.
Escribe una función que reciba una lista de números y calcule su promedio. 
Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente.
"""

# Función que calcula el promedio de una lista de números
def calcular_promedio(numeros):
    # Verificamos si la lista está vacía
    if not numeros:
        # Si está vacía, lanzamos una excepción personalizada
        raise ValueError("La lista está vacía, no se puede calcular el promedio")
    
    # Si hay números, calculamos la suma y dividimos entre la cantidad de elementos
    return sum(numeros) / len(numeros)

# Bloque try para manejar posibles excepciones
try:
    # Lista de números de ejemplo (vacía en este caso)
    datos = []
    
    # Intentamos calcular el promedio
    print(calcular_promedio(datos))

# Capturamos la excepción ValueError lanzada por la función
except ValueError as e:
    # Mostramos un mensaje de error al usuario
    print(f"Error: {e}")

""" 11.
Escribe un programa que pida al usuario que introduzca su edad. 
Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado 
(por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
adecuadamente."""

def pedir_edad():
    try:
        # Pedimos al usuario que introduzca su edad
        edad = int(input("Introduce tu edad: "))
        
        # Validamos rango
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")  # lanzamos error si está fuera de rango
        
        print(f"Tu edad es {edad} años")

    except ValueError as e:  # captura ValueError personalizado
        print(f"Error: {e}")

# Llamamos a la función
pedir_edad()

"""12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. 
Usa la función map()"""


def longitudes_palabras(frase):
   
    # Separa la frase en una lista de palabras usando los espacios
    palabras = frase.split()
    
    # Aplica la función len a cada palabra usando map()
    longitudes = list(map(len, palabras))
    
    # Devuelve la lista con las longitudes de cada palabra
    return longitudes

reseña = "El producto llegó rápido y funciona perfectamente"

print(longitudes_palabras(reseña))

"""13. Genera una función la cual, para un conjunto de caracteres, 
devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
Las letras no pueden estar repetidas.
Usa la función map()"""

def letras_mayus_minus(caracteres):

    # Convierte la cadena en un conjunto para eliminar letras repetidas
    caracteres_unicos = set(caracteres)
    
    # Usa map() para transformar cada letra en una tupla (mayúscula, minúscula)
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))

hashtags = "DataScienceAI"

print(letras_mayus_minus(hashtags))

"""14. Crea una función que retorne las palabras de una 
lista de palabras que comience con una letra en especifico. 
Usa la función filter()"""


def palabras_por_letra(lista_palabras, letra):
    # Usa filter() para quedarse solo con las palabras que empiezan por la letra indicada
    # p.startswith(letra) devuelve True si la palabra comienza con esa letra
    return list(filter(lambda p: p.startswith(letra), lista_palabras))

# Lista de palabras de ejemplo (comentarios de clientes)
comentarios = ["producto", "precio", "calidad", "puntual", "perfecto", "servicio"]

print(palabras_por_letra(comentarios, "p"))

""" 15. 
Crea una función lambda que sume 3 a cada número de una lista dada.
"""
# Lista de ejemplo: ventas diarias de un producto
ventas = [10, 15, 20, 25]

# Usamos map() con lambda
ventas_mas_3 = list(map(lambda x: x + 3, ventas))

print(ventas_mas_3)


"""16. 
Escribe una función que tome una cadena de texto y un número entero n como parámetros 
y devuelva una lista de todas las palabras que sean más largas que n. 
Usa la función filter()"""


def palabras_mas_largas(texto, n):
    
    # Divide el texto en una lista de palabras usando los espacios
    palabras = texto.split()
    
    # Usa filter() para quedarse solo con las palabras cuya longitud sea mayor que n
    return list(filter(lambda p: len(p) > n, palabras))

comentario = "La aplicación educativa es muy intuitiva y excelente"

resultado = palabras_mas_largas(comentario, 6)

print(resultado)


"""
17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). 
Usa la función reduce()"""


from functools import reduce  # Importa reduce para aplicar una función acumulativa sobre la lista

def lista_a_numero(digitos):
    """
    Recibe una lista de dígitos y devuelve el número que forman
    """
    # reduce() recorre la lista y va multiplicando el acumulador por 10 y sumando el dígito actual
    # Ejemplo: [2,4,9,1] -> (((2*10 + 4)*10 + 9)*10 + 1) = 2491
    return reduce(lambda acc, d: acc * 10 + d, digitos)

codigo_verificacion = [2, 4, 9, 1]

print(lista_a_numero(codigo_verificacion))



""" 18. 
Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y 
use la función filter para extraer a los estudiantes con una calificación 
mayor o igual a 90. Usa la función filter()
"""

def estudiantes_destacados(estudiantes):
   
    # filter() recorre la lista de diccionarios y selecciona solo los que cumplen la condición
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

# Lista de estudiantes con su información
estudiantes = [
    {"nombre": "Ana", "edad": 15, "calificacion": 92},
    {"nombre": "Luis", "edad": 16, "calificacion": 85},
    {"nombre": "María", "edad": 15, "calificacion": 98},
    {"nombre": "Carlos", "edad": 17, "calificacion": 88},
    {"nombre": "Sofía", "edad": 16, "calificacion": 90}
]

destacados = estudiantes_destacados(estudiantes)

print(destacados)


"""
19. Crea una función lambda que filtre los números impares de una lista dada.
"""


# Lista de IDs de transacciones
ids_transacciones = [101, 102, 103, 104, 105, 106, 107]

# Usamos filter() con lambda para seleccionar solo los números impares
ids_reales = list(filter(lambda x: x % 2 != 0, ids_transacciones))

print(ids_reales)


"""20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. 
Usa la función filter()"""


# Función que filtra solo los elementos que sean enteros
def filtrar_enteros(datos):
    
    # filter() recorre la lista y mantiene los elementos que cumplan la condición del lambda
    # isinstance(x, int) devuelve True si x es un entero
    return list(filter(lambda x: isinstance(x, int), datos))

# Lista de ejemplo con enteros y strings
datos = [23, "error", 45, "N/A", 12, "desconocido", 0]

resultado = filtrar_enteros(datos)

print(resultado)

"""
21. Crea una función que calcule el cubo de un número dado mediante una función lambda
"""

# Lista de puntuaciones de estudiantes
puntuaciones = [2, 3, 5, 4, 6]

# Calcular el cubo de cada puntuación directamente con lambda
puntuaciones_cubo = list(map(lambda x: x**3, puntuaciones))

print("Puntuaciones originales:", puntuaciones)
print("Puntuaciones elevadas al cubo:", puntuaciones_cubo)

"""
22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.
Usa la función reduce()."""

from functools import reduce

# Ventas diarias de un producto en 5 días
ventas_diarias = [3, 5, 2, 4, 6]  # unidades vendidas

# Producto total usando reduce
producto_total = reduce(lambda x, y: x * y, ventas_diarias)

print("Producto total de unidades vendidas:", producto_total)


"""
23. Concatena una lista de palabras. Usa la función reduce().
"""

from functools import reduce

# Lista de palabras que describen un producto
etiquetas_producto = ["innovador", "educativo", "interactivo", "IA"]

# reduce() recorre la lista y aplica la función lambda a cada par de elementos
# lambda x, y: x + " " + y → concatena cada palabra con un espacio entre ellas
descripcion = reduce(lambda x, y: x + " " + y, etiquetas_producto)

print("Descripción del producto:", descripcion)

"""
24. Calcula la diferencia total en los valores de una lista. 
Usa la función reduce()."""

from functools import reduce

ventas_diarias = [150, 200, 180, 220, 190, 210, 230]

# Emparejamos cada día con el siguiente y sumamos las diferencias absolutas
diferencia_total = reduce(
    lambda total, par: total + abs(par[1] - par[0]),
    zip(ventas_diarias[:-1], ventas_diarias[1:]),
    0
)

print("Diferencia total:", diferencia_total)


"""
25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

# Definimos la función contar_caracteres que recibe un string
def contar_caracteres(texto):
   
    # len() devuelve la longitud de la cadena, incluyendo espacios y signos
    return len(texto)

nombre_cliente = "Mabel Rivera"

print("Número de caracteres:", contar_caracteres(nombre_cliente))


"""26. Crea una función lambda que calcule el resto de la división entre dos números dados."""


# Definimos una función lambda que recibe dos parámetros y devuelve el resto de la división
resto = lambda total, capacidad: total % capacidad

# Ejemplo: número de productos y capacidad de cada caja
productos = 12
capacidad_caja = 5

sobran = resto(productos, capacidad_caja)

print(sobran)

"""
27. Crea una función que calcule el promedio de una lista de números.
"""

# Definimos la función que recibe una lista de números y devuelve su promedio
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)  # suma todos los elementos y divide entre la cantidad

# Ejemplo: ventas semanales de un producto en miles de euros
ventas = [120, 150, 100, 130, 170, 160, 140]

# Calculamos el promedio de ventas
promedio = calcular_promedio(ventas)

# Mostramos el resultado
print(promedio)

"""28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""

def primer_duplicado(lista):
    vistos = set()   # aquí guardamos lo que ya vimos

    for elemento in lista:
        if elemento in vistos:
            return elemento   # primer duplicado encontrado
        vistos.add(elemento)

    return None   # si no hay duplicados

clientes = [101, 203, 405, 203, 507, 101]

duplicado = primer_duplicado(clientes)

print(duplicado)

"""29. Crea una función que convierta una variable en una cadena de texto 
y enmascare todos los caracteres con el carácter '#', 
excepto los últimos cuatro."""

def enmascarar_variable(valor):
    # Convertir a string por si no lo es
    valor_str = str(valor)
    
    # Tomar los últimos 4 caracteres
    ultimos_cuatro = valor_str[-4:]
    
    # Enmascarar el resto con '#'
    enmascarado = '#' * (len(valor_str) - 4) + ultimos_cuatro
    
    return enmascarado

tarjeta = 1234567890123456
print(enmascarar_variable(tarjeta))


"""30. Crea una función que determine si dos palabras son anagramas, 
es decir, si están formadas por las mismas letras pero en diferente orden."""

def son_anagramas(palabra1, palabra2):
    # Convertir ambas palabras a minúsculas para ignorar mayúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Ordenar las letras de cada palabra y comparar
    return sorted(palabra1) == sorted(palabra2)

pares = [
    ("datos", "sadto"),
    ("redes", "sedre"),
    ("tabla", "balta"),
    ("modelo", "delomo"),
    ("clase", "secal")
]

# Probar la función con los pares
for p1, p2 in pares:
    resultado = son_anagramas(p1, p2)
    print(f"'{p1}' y '{p2}' son anagramas? {resultado}")

"""31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""

def buscar_cliente():
    try:
        # Pedimos al usuario que ingrese los nombres separados por coma
        lista_clientes = input("Ingrese los nombres de los clientes separados por coma: ").split(",")
        lista_clientes = [nombre.strip() for nombre in lista_clientes]  # Limpiamos espacios
        
        # Pedimos el nombre a buscar
        nombre_buscar = input("Ingrese el nombre del cliente a buscar: ").strip()
        
        # Comprobamos si el nombre está en la lista
        if nombre_buscar not in lista_clientes:
            raise ValueError(f"❌ Cliente '{nombre_buscar}' no encontrado.")  # Lanzamos excepción
        
        # Si está, imprimimos mensaje
        print(f"✅ Cliente '{nombre_buscar}' encontrado.")
    
    except ValueError as e:
        print(e)  # Mostramos el mensaje de error

# Llamamos a la función
buscar_cliente()


""" 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí."""

def buscar_puesto(nombre_completo, lista_empleados):
    """
    Busca un empleado en la lista y devuelve su puesto.
    """
    
    # Verificamos si el nombre está en la lista de empleados
    if nombre_completo in lista_empleados:
        return f"{nombre_completo} ocupa el puesto de {lista_empleados[nombre_completo]}"
    else:
        return f"{nombre_completo} no trabaja aquí."

# Lista de empleados ejemplo (diccionario: nombre -> puesto)
empleados = {
    "Juan Pérez": "Analista de Datos",
    "Ana Gómez": "Gerente de Marketing",
    "Carlos López": "Desarrollador Python",
    "María Rodríguez": "Diseñadora UX"
}

# Ejemplo de uso
nombre = input("Ingrese el nombre completo del empleado: ").strip()
resultado = buscar_puesto(nombre, empleados)
print(resultado)

"""33. Crea una función lambda que sume elementos correspondientes de dos listas dadas."""

# Ventas de la Sucursal A y Sucursal B por día
ventas_sucursal_A = [150, 200, 175, 300, 250] 
ventas_sucursal_B = [100, 180, 220, 310, 270] 

# Lambda para sumar ventas correspondientes
total_diario = lambda v1, v2: [x + y for x, y in zip(v1, v2)]

# Calculamos el total diario
ventas_totales = total_diario(ventas_sucursal_A, ventas_sucursal_B)

print("Ventas totales por día:", ventas_totales)


"""34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
El objetivo es implementar estos métodos para manipular la estructura del árbol.

Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
mismas.

Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol."""

class Arbol:
    def __init__(self):
        """Inicializa un árbol con tronco de longitud 1 y lista vacía de ramas"""
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en 1"""
        self.tronco += 1
        print(f"El tronco ahora mide {self.tronco} unidades.")

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1"""
        self.ramas.append(1)
        print(f"Se añadió una nueva rama. Total de ramas: {len(self.ramas)}")

    def crecer_ramas(self):
        """Aumenta en 1 la longitud de todas las ramas existentes"""
        if not self.ramas:
            print("No hay ramas para crecer.")
            return
        self.ramas = [r + 1 for r in self.ramas]
        print(f"Todas las ramas crecieron. Longitudes actuales: {self.ramas}")

    def quitar_rama(self, posicion):
        """Elimina la rama en la posición especificada (empezando desde 0)"""
        if 0 <= posicion < len(self.ramas):
            rama_eliminada = self.ramas.pop(posicion)
            print(f"Se eliminó la rama en posición {posicion} (longitud {rama_eliminada}).")
        else:
            print("Posición inválida. No se pudo eliminar la rama.")

    def info_arbol(self):
        """Devuelve información del árbol"""
        info = {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy()
        }
        return info

# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco
mi_arbol.crecer_tronco()  # Tronco pasa de 1 a 2

# 3. Añadir una nueva rama
mi_arbol.nueva_rama()      # Se añade rama de longitud 1

# 4. Hacer crecer todas las ramas
mi_arbol.crecer_ramas()     # La rama pasa de 1 a 2

# 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()       # Rama de longitud 1
mi_arbol.nueva_rama()       # Otra rama de longitud 1

# 6. Retirar la rama situada en la posición 2 (tercera rama)
mi_arbol.quitar_rama(2)

# 7. Obtener información del árbol
info = mi_arbol.info_arbol()
print("Información del árbol:")
print(info)


"""35. No hay enunciado para este número"""

"""36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.

Código a seguir:

1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

Caso de uso:

1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
PROYECTO LÓGICA: Katas de Python 2
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
"""

class UsuarioBanco:
    def __init__(self, nombre, saldo=0, cuenta_corriente=False):
        """Inicializa un usuario con nombre, saldo y si tiene cuenta corriente"""
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Retira dinero del saldo si hay suficiente, sino lanza error"""
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} retiró {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, usuario_origen, cantidad):
        """Transfiere dinero desde otro usuario si tiene saldo suficiente"""
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if cantidad > usuario_origen.saldo:
            raise ValueError(f"{usuario_origen.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        usuario_origen.saldo -= cantidad
        self.saldo += cantidad
        print(f"{usuario_origen.nombre} transfirió {cantidad} a {self.nombre}.")
        print(f"Saldo {usuario_origen.nombre}: {usuario_origen.saldo}")
        print(f"Saldo {self.nombre}: {self.saldo}")

    def agregar_dinero(self, cantidad):
        """Agrega dinero al saldo"""
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad
        print(f"{self.nombre} agregó {cantidad}. Saldo actual: {self.saldo}")

# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", saldo=100, cuenta_corriente=True)
bob = UsuarioBanco("Bob", saldo=50, cuenta_corriente=True)

# 2. Agregar 20 unidades de saldo a Bob
try:
    bob.agregar_dinero(20)
except ValueError as e:
    print(e)

# 3. Hacer una transferencia de 80 unidades desde Bob a Alicia
try:
    alicia.transferir_dinero(bob, 80)
except ValueError as e:
    print(e)

# 4. Retirar 50 unidades de saldo a Alicia
try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print(e)

"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,reemplazar_palabras , 
eliminar_palabra . 

Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra nueva . 
Tiene que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar
texto"""

from collections import Counter

# 1️⃣ Contar palabras
def contar_palabras(texto):
    palabras = texto.split()
    conteo = Counter(palabras)
    return dict(conteo)

# 2️⃣ Reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# 3️⃣ Eliminar palabra
def eliminar_palabra(texto, palabra_eliminar):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_eliminar]
    return " ".join(palabras_filtradas)

# 4️⃣ Función procesar_texto que llama a las anteriores
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se necesitan dos argumentos: palabra_original, palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se necesita un argumento: palabra a eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción inválida. Usa 'contar', 'reemplazar' o 'eliminar'.")

log_clientes = "error login error pago correcto error login fallo pago correcto fallo pago"

resultado = procesar_texto(log_clientes, "contar")
print(resultado)

nuevo_log = procesar_texto(log_clientes, "reemplazar", "fallo", "error")
print(nuevo_log)

log_filtrado = procesar_texto(log_clientes, "eliminar", "correcto")
print(log_filtrado)


"""38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
"""

# Pedimos al usuario que ingrese la hora en formato 24h
hora = int(input("Introduce la hora (0-23): "))

# Validamos que la hora sea correcta
if hora < 0 or hora > 23:
    print("Hora inválida. Debe estar entre 0 y 23.")
else:
    # Clasificamos según rangos de horas
    if 6 <= hora < 12:
        print("Buenos días 🌞")
    elif 12 <= hora < 18:
        print("Buenas tardes ☀️")
    else:
        print("Buenas noches 🌙")

hora = int(input("Introduce la hora (0-23): "))


"""39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
"""

# Pedimos al usuario la calificación numérica
calificacion = int(input("Introduce la calificación del alumno (0-100): "))

# Validamos que la calificación esté en el rango correcto
if calificacion < 0 or calificacion > 100:
    print("Calificación inválida. Debe estar entre 0 y 100.")
else:
    # Determinamos la calificación en texto según el rango
    if 0 <= calificacion <= 69:
        texto = "Insuficiente"
    elif 70 <= calificacion <= 79:
        texto = "Bien"
    elif 80 <= calificacion <= 89:
        texto = "Muy bien"
    else:  # 90 - 100
        texto = "Excelente"
    
    print(f"La calificación en texto es: {texto}")


"""40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo"
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
"""

def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica.
    
    Parámetros:
    - figura: "rectangulo" o "triangulo"
    - datos: tupla con los datos necesarios
        * Rectángulo: (ancho, alto)
        * Triángulo: (base, altura)
        
    Devuelve:
    - Área de la figura
    """
    if figura.lower() == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Para un rectángulo necesitas ancho y alto")
        ancho, alto = datos
        return ancho * alto
    
    elif figura.lower() == "triangulo":
        if len(datos) != 2:
            raise ValueError("Para un triángulo necesitas base y altura")
        base, altura = datos
        return (base * altura) / 2
    
    else:
        raise ValueError("Figura no válida. Usa 'rectangulo' o 'triangulo'")

# Ejemplos de uso
area_rect = calcular_area("rectangulo", (25, 12))
print(f"Área del rectángulo: {area_rect}")

area_tri = calcular_area("triangulo", (6, 8))
print(f"Área del triángulo: {area_tri}")


"""41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python.
"""

# 1️⃣ Solicitar el precio original
precio_original = float(input("Introduce el precio del artículo (€): "))

# 2️⃣ Preguntar si tiene un cupón de descuento
tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

# 3️⃣ Inicializamos el precio final igual al precio original
precio_final = precio_original

# 4️⃣ Aplicar descuento si tiene cupón
if tiene_cupon in ["sí", "si"]:
    valor_cupon = float(input("Introduce el valor del cupón (€): "))
    
    if valor_cupon > 0:
        precio_final -= valor_cupon  # Restamos el descuento
        print(f"Se aplicó un descuento de {valor_cupon}€. ")
    else:
        print("Cupón inválido. No se aplicará descuento.")
elif tiene_cupon == "no":
    print("No hay cupón, el precio se mantiene.")
else:
    print("Respuesta no válida, se asumirá sin cupón.")

# 5️⃣ Mostrar el precio final
print(f"El precio final de la compra es: {precio_final:.2f} €")
