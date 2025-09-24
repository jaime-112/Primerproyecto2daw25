# Ejercicios de listas

# Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo.
#  Muestra el máximo de los números guardado en la lista, muestra los números pares.

num1 = int(input("Inserte un número: "))

lista1 = []

while num1 > 0:
    lista1.append(num1)
    num1 = int(input("Inserte un número: "))

print("El número máximo: %d " % max(lista1))
            
print()

for i1 in lista1:
    if i1 % 2 == 0:
        print("El número ", i1, " es par")

# Realizar un programa que, dada una lista, 
# devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, 
# dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], 

lista2 = ['Di', 'buen', 'día', 'a', 'papa']
print(lista2[::-1])




lista3 = ['Di', 'buen', 'dia', 'a', 'papa', "hola", "papa", "buen", "dia"]

cadena3 = input("Cadena:")
if cadena3 in lista3:
    print("La cadena está en la lista")
else:
    print("La cadena no está en la lista")

print(lista3.count(cadena3))

cadena3b = input("Cadena a reemplazar:")
num3 = lista3.count(cadena3)
pos3 = 0
for i3 in range(0, num3):
    pos3 = lista3.index(cadena3, pos3)
    lista3[pos3] = cadena3b
print(lista3)


# # Dado una lista, hacer un programa que indique si está ordenada o no.

lista4 = [2, 3, 4, 1]
lista4b = lista4[:]
lista4.sort()
if lista4 == lista4b:
    print("Lista ordenada")
else:
    print("Lista no ordenada")




# Ejercicios de cadenas





# Crear un programa que lea por teclado una cadena y un carácter,
# e inserte el carácter entre cada letra de la cadena. 
# Ej: separar y , debería devolver s,e,p,a,r,a,r

cadena5 = input("Cadena:")
caracter5 = input("Carácter:")
print(caracter5.join(cadena5))



# Crear un programa que lea por teclado una cadena y un carácter, 
# y reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
cadena6 = input("Cadena:")
caracter6 = input("Carácter:")
for i6 in range(10):
    cadena6 = cadena6.replace(str(i6), caracter6)
print(cadena6)


# Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
# Dicha cadena con la primera letra de cada palabra en mayúsculas.
#  Por ejemplo, si recibe república argentina debe devolver República Argentina.
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.


# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
cadena7 = input("Cadena:")
lista7 = cadena7.split(" ")
for i7 in lista7:
    print(i7[0], end="")
print()

for i7 in lista7:
    print(i7.capitalize(), end=" ")
print()

for i7 in lista7:
    if i7.startswith("a") or i7.startswith("A"):
        print(i7, end=",")
print()

# Escribir funciones que dadas dos cadenas de caracteres:

# Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
# Devuelva la que sea anterior en orden alfabético. Por ejemplo, si recibe kde y gnome debe devolver gnome.

cadena8a = input("Cadena 1:")
cadena8b = input("Cadena 2:")
if cadena8a.find(cadena8b) > -1:
    print("cadena8b es subcadena de cadena8a")
else:
    print("cadena8b no es subcadena de cadena8a")

print(cadena8a if cadena8a < cadena8b else cadena8b)

# Escribir un programa python que dado una palabra diga si es un palíndromo.
# Un palídromo Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer


cadena9 = input("Cadena:")
if cadena9.lower() == cadena9[::-1].lower():
    print("palindromo")
else:
    print("no palindromo")


