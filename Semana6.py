# Ejercicio 1: Multiplicar todos los elementos por 3
print("Ejercicio 1: Multiplicar todos los elementos por 3\n")
numeros = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 3, numeros)),"\n")

#Ejercicio 2: Filtrar números mayores a 10
print("Ejercicio 2: Filtrar números mayores a 10\n")
#Dada una lista de números, filtra los números que son mayores a 10.
numeros = [5, 10, 15, 20, 25]
print(list(filter(lambda x: x > 10, numeros)),"\n")

#Ejercicio 3: Convertir una lista de palabras a mayúsculas
print("Ejercicio 3: Convertir una lista de palabras a mayúsculas\n")
#Dada una lista de palabras, conviértelas todas a mayúsculas.
palabras = ["hola", "mundo", "python"]
print(list(map(lambda x: x.upper(), palabras)),"\n")

#Ejercicio 4: Filtrar palabras que empiezan con 'p'
print("Ejercicio 4: Filtrar palabras que empiezan con 'p'\n")
#Dada una lista de palabras, filtra aquellas que comienzan con la letra 'p'.
palabras = ["hola", "mundo", "python", "programacion"]
print(list(filter(lambda x: x.startswith('p'), palabras)),"\n")

#Ejercicio 5: Calcular la longitud de cada palabra
print("Ejercicio 5: Calcular la longitud de cada palabra")
#Dada una lista de palabras, calcula la longitud de cada una.
palabras = ["hola", "mundo", "python"]
print(list(map(lambda x: len(x), palabras)),"\n")

# Ejercicio 6: Filtrar palabras con longitud mayor a 4
print("Ejercicio 6: Filtrar palabras con longitud mayor a 4\n")
palabras = ["hola", "mundo", "python", "hi"]
print(list(filter(lambda x: len(x) > 4, palabras)),"\n")

# Ejercicio 7: Convertir una lista de temperaturas de Celsius a Fahrenheit
print("Ejercicio 7: Convertir una lista de temperaturas de Celsius a Fahrenheit\n")
celsius = [0, 20, 37, 100]
print(list(map(lambda x: (x * 9/5) + 32, celsius)),"\n")

# Ejercicio 8: Filtrar temperaturas mayores a 50 grados Fahrenheit
print("Ejercicio 8: Filtrar temperaturas mayores a 50 grados Fahrenheit")
fahrenheit = [32.0, 68.0, 98.6, 212.0]
print(list(filter(lambda x: x > 50, fahrenheit)),"\n")

# Ejercicio 9: Sumar 5 a todos los elementos de una lista
print("Ejercicio 9: Sumar 5 a todos los elementos de una lista\n")
numeros = [1, 2, 3, 4, 5]
print(list(map(lambda x: x + 5, numeros)),"\n")

# Ejercicio 10: Filtrar palabras que contienen la letra 'a'
print("Ejercicio 10: Filtrar palabras que contienen la letra 'a'\n")
palabras = ["hola", "mundo", "python", "vida"]
print(list(filter(lambda x: 'a' in x, palabras)),"\n")


