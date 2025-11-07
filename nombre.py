bd = []

def agregar_nombre(nombre):
    bd.append(nombre)
    print(f"Nombre '{nombre}' agregado a la base de datos.")
    
def mostrar_nombres():
    print("Nombres en la base de datos:")
    for nombre in bd:
        print(nombre)
        
n = int(input("¿Cuántos nombres desea agregar a la base de datos? "))

for _ in range(n):
    nombre = input("Digite un nombre: ")
    agregar_nombre(nombre)
    
opcion = int(input("Digite la opcion deseada: 1. Mostrar todos los nombres, 2. validar si existe un nombre e imprimirlo, 3. Salir: "))

if opcion == 1:
    mostrar_nombres()
elif opcion == 2:
    nombre_a_validar = input("Digite el nombre que desea validar: ")
    if nombre_a_validar in bd:
        print(f"El nombre '{nombre_a_validar}' existe en la base de datos.")
    else:
        print(f"El nombre '{nombre_a_validar}' no se encuentra en la base de datos.")
elif opcion == 3:
    print("Saliendo del programa.")
else:
    print("Opción no válida")
    