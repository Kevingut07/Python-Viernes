piramide = []

n = int(input("Digite la altura de la piramide: "))

for i in range(1, n + 1):
    fila = []
    for j in range(i):
        fila.append('*')
    piramide.append(fila)

impresion = int(input("Digite 1 para imprimir la piramide de forma normal o 2 para imprimirla invertida: "))

if impresion == 1:   
    for fila in piramide:
     print(' '.join(fila))
elif impresion == 2: 
    piramide.sort(reverse=True)
    for fila in piramide:
     print(' '.join(fila))    
else:
    print("Opcion no valida")


    
