def conversor (tipo_pesos, valor_dolares):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = round(pesos / valor_dolares, 3)
    dolares = str(dolares)
    print("Tienes $" + dolares + " USD")

menu = """ Bienvenido al conversor de moneada.
las opciones son :

1 - ARS
2 - COP
3 - MXN

Elige una de las opciones: """

opcion = int(input(menu))


if opcion == 1:
    conversor("Argentinos", 65)
elif opcion == 2:
    conversor("Colombanos", 3750)
elif opcion == 3:
    conversor("Mexicanos", 25)
else:
    print("Por favor eleige una de las opciones")

# en la poxima vesio se agregaran funciooes con def

#Ya se se ha puesto la funciom