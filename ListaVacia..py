departamentos_colombia = []


num_departamentos = int(input("Ingrese la cantidad de departamentos a ingresar: "))


for i in range(num_departamentos):
    departamento = input("Ingrese el nombre del departamento de Colombia: ")
    departamentos_colombia.append(departamento)

departamentos_colombia.sort(reverse=True)

# Imprimimos la lista ordenada
print("Lista de departamentos de Colombia ordenada en orden descendente:", departamentos_colombia)

# Imprimimos los 2 últimos departamentos ingresados
print("Los 2 últimos departamentos ingresados son:", departamentos_colombia[-2:])
