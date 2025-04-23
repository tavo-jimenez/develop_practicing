# Ejercicio 1: Crear una lista de nombres y verificar si un nombre específico está
#  en la lista.
#names = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis']

# names = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis']
# buscado = input("Nombre: ").strip()
# print("Sí está" if buscado in names else "No está")

# Ejercicio 2: Crear una lista de números y calcular la suma de todos los elementos.
#numbers = [10, 20, 30, 40, 50]

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for n in numbers:
#     total += n
# print(total)

# Ejercicio 5: Crear una lista de números y eliminar todos los números impares.
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = [n for n in numbers if n % 2 == 0]
print(numbers) 
