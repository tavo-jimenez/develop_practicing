# edad = int(input("Cual es tu edad?"))
# tieneDinero = input("tienes dinero para pagar?")

# if tieneDinero.lower() == 'si tengo' or tieneDinero.lower() == 'sí tengo' or tieneDinero.lower() == 'si':
#     if edad > 18:
#         print('Comida McDonalds')
#     else:
#         print('Comida saludable')
# elif tieneDinero.lower() == 'no, pero me regalas':
#     print('Ok, no hay problema. Toma.')
# else:
#     print('No podemos entregar tu comida')

# if (tieneDinero.lower() == 'si tengo' or tieneDinero.lower() == 'sí' or tieneDinero.lower() == 'si') and edad >= 18:
#     print('Comida McDonalds')
# elif (tieneDinero.lower() == 'si tengo' or tieneDinero.lower() == 'sí' or tieneDinero.lower() == 'si') and edad < 18:
#     print('Comida saludable')
# elif tieneDinero.lower() == 'no, pero me regalas':
#     print('Ok, no hay problema. Toma.')
# else:
#     print('No podemos entregar tu comida')

# Escribe un programa que pida al usuario un número y luego imprima si el número es
# positivo, negativo o cero

# numero = float(input("Ingresa un número: "))

# if numero > 0:
#     print("El número es positivo.")
# elif numero < 0:
#     print("El número es negativo.")
# else:
#     print("El número es cero.")

# for i in range(1, 101):
#     print(i)

while True:
    try:
        numero = int(input("Ingresa un número: "))
        if numero % 2 == 0:
            print("Es par")
        else:
            print("Es impar")
        break  
    except ValueError:
        print("¡Entrada no válida! Por favor, ingresa un número entero.")
