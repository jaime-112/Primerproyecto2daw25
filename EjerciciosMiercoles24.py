# Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo.
#  Muestra el máximo de los números guardado en la lista, muestra los números pares.

num1 = int(input("Inserte un número: "))

lista = []

while num1>0:
    lista.append(num1)
    num1 = int(input("Inserte un número: "))

print("El número máximo: %d " % max(lista))
            
print()

for i in lista:
    if i%2 == 0:
        print("El número ",i," es par")

# Realizar un programa que, dada una lista, 
# devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, 
# dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], 

lista2 = ['Di', 'buen', 'día', 'a', 'papa']
print (lista2[::-1])




# Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, 
# indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera por la segunda en la lista,
# y por último borra la cadena de la lista

lista3=['Di', 'buen', 'dia', 'a', 'papa',"hola","papa","buen","dia"]	

cadena=input("Cadena:")
if cadena in lista3:
	print("La cadena está en la lista")
else:
	print("La cadena no está en la lista")	

print(lista3.count(cadena))	

cadena2=input("Cadena a reemplazar:")
num=lista3.count(cadena)
pos=0
for i in range(0,num):
	pos=lista3.index(cadena,pos)
	lista3[pos]=cadena2
print(lista3)


# Dado una lista, hacer un programa que indique si está ordenada o no.

lista=[2,3,4,1]
lista2=lista[:]
lista.sort()
if lista==lista2:
	print("Lista ordenada")
else:
	print("Lista no ordenada")