agenda = {}

while True:
    nombre = input("Ingrese el nombre del contacto (o 'fin' para terminar): ")
    if nombre == "fin":
        break
    
    if nombre in agenda:
        print("El nombre ya existe en la agenda, ingrese otro.")
        continue
    
    telefono = input("Ingrese el teléfono del contacto: ")
    agenda[nombre] = telefono

print("Agenda completa:")
print(agenda)

while True:
    nombre_buscar = input("Ingrese el nombre del contacto para buscar su teléfono (o 'fin' para terminar): ")
    if nombre_buscar == "fin":
        break
    
    if nombre_buscar in agenda:
        telefono = agenda[nombre_buscar]
        print("El teléfono de", nombre_buscar, "es:", telefono)
    else:
        print("El nombre ingresado no se encuentra en la agenda.")
