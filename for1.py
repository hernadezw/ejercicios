# num=int(input("Ingrese un numero de 4    digitos: ")) #3525
# den=1000
# if 1<num<9999:
#     for i in range(1,5,1):
#         d=num//den
#         num=num%den
#         den=den//10
#         contador=contador+1
#         print(d) 
# else:
#     print("Numero no valido")
# num=int(input("Ingrese la tabla a multiplicar: ")) 

# for i in range(1,num):
#     print(i,":" ,i*num)
# Almacena el actual número más grande aquí.
# numero_mayor = -999999999
# numero = int(input("Introduce un número o escribe -1 para detener: "))
# while numero != -1:
#     if numero > numero_mayor:
#         # Sí si, se actualiza numero_mayor.
#         numero_mayor = numero
#     # Ingresa el siguiente número.
#     numero = int(input("Introduce un número o escribe -1 para detener: "))
# print("El número más grande es:", numero_mayor)

# numero_mayor= 1000
# numero=int(input("Ingrese un numero o ingrese -1 para terminar: "))#12

# while numero != -1:
#     if numero>numero_mayor:
#         numero_mayor=numero
#     numero=int(input("Ingrese un numero o ingrese -1 para terminar: "))#85
# print("El numero mas grande es: ", numero_mayor)

# while True:
#     print("Estoy atrapado")


# impar=0
# par=0
# for i in range(m, 0, -1):    
#     print(" " * (m - i), "*" * (2 * i - 1))
# numero=int(input("Ingrese numeros o presione 0:"))
# while numero != 0:
#     if numero%2==1:
#         impar= impar+1
#     else:
#         par=par+1
#     numero=int(input("Ingrese numeros o presione 0: "))
# print("Impares: ", impar)
# print("Pares: ", par)
# tabla=int(input("Ingrese la tabla que desea multiplicar: "))#8
# repeticiones=int(input("Hasta cuántas veces deseas multiplicar: "))#2
# for i in range(1,repeticiones+1):
#     print(i,": ", i,"*", tabla,"=", tabla*i)

# n = int(input("Introduce el número de filas (un número impar): ")) #7
# m = n // 2 #3
# for i in range(1, m + 1):#3   
#     print(" " * (m - i), "*" * (2 * i - 1))
# print("*" * n)    

# for i in range(m, 0, -1):    
#     print(" " * (m - i), "*" * (2 * i - 1))

for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")