

numeros = []


while True:
    num = input("Ingrese un número entero (o 'fin' para terminar): ")
    if num == 'fin':
        break
    try:
        num = int(num)
        numeros.append(num)
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Ordenamos la lista de forma ascendente y descendente
ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)


print("Lista ordenada de forma ascendente:", ascendente)
print("Lista ordenada de forma descendente:", descendente)
