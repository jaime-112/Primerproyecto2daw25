# # 1. Sumar todos los elementos de una lista
# num = int(input("Inserte un numero: "))


# suma = 0
# while num > 0:
#     suma += num
#     num = int(input("Inserte otro numero: "))


# print("La suma de todos los numeros introducidos es: ",suma)



# 2. Encontrar el mayor y el menor

# num1 = int(input("Inserte un numero: "))
# num2 = int(input("Inserte un segundo numero: "))
# num3 = int(input("Inserte un tercer numero: "))

# mayor= 0
# medio = 0
# menor= 0

# if num1 > num2 and num1>num3:
#     mayor= num1

#     if num2>num3:
#         medio = num2
#         menor = num3
#     else:
#         medio = num3
#         menor = num2

# elif num2 > num1 and num2 > num3:
#     mayor = num2

#     if num1 > num3:
#         medio = num1
#         menor = num3
#     else:
#         medio = num3
#         menor = num1

# else:
#     mayor = num3
#     if num1>num2:
#         medio = num1
#         menor = num2
#     else:
#         medio = num2
#         menor = num1



# print("Mayor: ",mayor," Medio: ",medio," Menor: ",menor)


# 2. Encontrar el mayor y el menor con lista


# lista = [1,2,3,4,55,6,7,8,9,33,0,-77]
# mayor = 0
# for x in lista:

#     if x > mayor:
#         mayor=x
        
# menor = mayor

# for i in lista:
#     if i < menor:
#         menor = i
    

# print("El mayor es: ",mayor)
# print ("El menor es: ", menor)




# 3. Contar repeticiones


lista= ["mi", "nombre", "es", "Jaime", "me", "llamo",
         "Jaime", "mi", "color", "favorito", "es", 
        "el", "rojo", "mi", "comida", "favorita", 
        "es", "carne"]

contadordecadena= 0

text = input("Inserte la palabra que quiera buscar en la lista: ")

for x in lista:

    if x == text:
        contadordecadena += 1


print(" la cadena: ",text, " Se encuentra en la lista: ",contadordecadena, " veces")
