n = 5

for fila in range(n):
    linea = ""
    for col in range(n):
        if fila == 0 or fila == n-1 or col == 0 or col == n-1:
            linea += "x "
        else:
            linea += "- "
    print(linea)
