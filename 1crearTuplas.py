numeros = (2, 4, 7, 9, 10, 13)
par = ()
impar = ()

for numero in numeros:
    if numero % 2 == 0:
        par += (numero,)
    else:
        impar += (numero,)

print("Números pares:", par)
print("Números impares:", impar)

