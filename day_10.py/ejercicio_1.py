# Iterate 0 to 10 using for loop, do the same using while loop.

for i in range (11):
    print(i)

i = 0
while i < 11:
    print(i)
    i = i + 1     #prints from 0 to 11

# Iterate 10 to 0 using for loop, do the same using while loop.

i = 10
while i >= 0:
    print(i)
    i -= 1 
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("escalera de tringulos")   

for i in range (1,8):
     print ('#' * i)

# Utilice bucles anidados para crear lo siguiente:
print("cuadrado")  

for i in range (8): 
    for j in range (8):
        print('#', end= ' ')
    print()

# tabla de multiplicar
print("multiplicacion")

for i in range (11):
    print (f"{i}x{i}={i*i}")

# Iterate a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un for bucle e imprimiendo los artículos.
    
fruts =  ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
print("lista de elemtos")
for item in fruts:
    print(item)

# Uso para bucle para iterate de 0 a 100 e imprimir sólo números pares
print("nuemeros pares del 0 al 100")
for i in range(0,102,2):
    print(i)

# so para bucle para iterate de 0 a 100 e imprimir sólo números impares
    
print("nuemeros impares del 0 al 100")
for i in range(0,100,3):
    print(i)








