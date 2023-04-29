tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

indice = int(input("Ingrese un índice para mostrar el valor correspondiente: "))

if indice < 0 or indice >= len(tupla):
    print("El índice ingresado es inválido.")
else:
    valor = tupla[indice]
    print("El valor correspondiente al índice", indice, "es:", valor)
