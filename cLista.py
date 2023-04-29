"""
 El índice `-0` es equivalente al índice `0`, por lo que no hay ningún error en la primera línea. 
Sin embargo, en la segunda línea se está intentando acceder a un elemento de la lista utilizando un índice 
que está fuera de los límites de la lista.

La lista lista_colores tiene tres elementos, por lo que los índices válidos son 0, 1 y 2. 
Al intentar acceder al elemento -4, se está intentando acceder a un elemento que está cuatro posiciones antes del último elemento, 
lo cual es incorrecto.

El código corregido quedaría así:


lista_colores = ["rojo", "azul", "verde"]
print(lista_colores[0])
print(lista_colores[-3])


En la segunda línea, utilizamos el índice `-3`, que es equivalente al índice `0` en este caso.
"""