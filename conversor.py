menu = """ Bienvenido al conversor de moneada.
las opciones son :

1 - ARS
2 - COP
3 - MXN

Elige una de las opciones: """

opcion = int(input(menu))


if opcion == 1:
    pesos = float(input("¿Cuantos pesos argentinos tienes?: "))
    valor_dolar = 65
    dolares = pesos / valor_dolar
    print(" Tiene " + str(dolares) + " USD")
elif opcion == 2:
    pesos = float(input("¿Cuantos pesos mexicnaos tienes?: "))
    valor_dolar = 25
    dolares = pesos / valor_dolar
    print(" Tiene " + str(dolares) + " USD")
elif opcion == 3:
    pesos = float(input("¿Cuantos pesos colombianos tienes?: "))
    valor_dolar = 3750
    dolares = pesos / valor_dolar
    print(" Tiene " + str(dolares) + " USD")
else:
    print("Por favor eleige una de las opciones")

# en la poxima vesio se agregaran funciooes con def