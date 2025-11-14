# Tamaño del medio diamante
n = 7

# Parte superior
for i in range(1, n + 1):
    if i == 1 or i % 2 != 0:
        print(" " * (n - i) + "x " * i)




# Parte inferior
for i in range(n, 0, -1):
    if i == 1 or i % 2 != 0:
        print(" " * (n - i) + "x " * i)
