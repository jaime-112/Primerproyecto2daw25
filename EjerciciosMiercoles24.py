# Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo.
#  Muestra el máximo de los números guardado en la lista, muestra los números pares.

num1 = int(input("Inserte un número: "))

lista = []

while num1>0:
    lista.append(num1)
    num1 = int(input("Inserte un número: "))

print("El número máximo: %d " % max(lista))

for i in lista:
    if i%2 == 0:
        print("El número ",i," es par")
        print()