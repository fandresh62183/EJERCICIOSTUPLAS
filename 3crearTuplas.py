tupla = (2, 5, 3, 5, 7, 5, 9, 5)
numero_buscar = int(input("Ingresa un número para buscar en la tupla: "))

if numero_buscar in tupla:
    cuenta = tupla.count(numero_buscar)
    print("El número", numero_buscar, "aparece", cuenta, "veces en la tupla.")
else:
    print("El número", numero_buscar, "no se encuentra en la tupla.")
