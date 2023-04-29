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
