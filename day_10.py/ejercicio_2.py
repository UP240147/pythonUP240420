# Utilícelo para el bucle para iterate de 0 a 100 e imprime la suma de todos los números.

total = 0
for i in range (101):
    total += i
print(f"\ntotal entre todas las sumas es {total}")

# Utilícese para bucle para iterate de 0 a 100 e imprimir la suma de todos los pares y la suma de todas las probabilidades.

even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"\nla suma de todos los numeros es {even_sum}. y la suma de todos los impares es {odd_sum}")