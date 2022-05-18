#####Laboratorio 1####
print("1. Ingresar el radio de un criculo del usuario y calcule el area (π*r²)")
print("2. Preguntar al usuario su nombre y lo salude con su nombre")
print("3. Ingresar dos numero y realizar toddas las operaciones aritmeticas")
print("4. Hallar la potencia de cualquier numero")
print("5. Resuelva la siguiente ecuacion y = (-b+(b²+c)^1/2)/2a")
ejercicio = int(input("\nDigite el número de ejercicio del cual desea ver la solución: "))


if ejercicio == 1:
    # 1. Ingresar el radio de un criculo del usuario y calcule el area (π*r²)
    print("-----EJERCICIO 1-----")
    valorPi = 3.14159265
    radioCirculo = int(
        input("Ingrese el radio del círculo para obtener el área: "))
    areaCirculo = valorPi * radioCirculo * radioCirculo
    print("El área del círculo de radio ", radioCirculo, " es: ", areaCirculo)

elif ejercicio == 2:
    # 6. Preguntar al usuario su nombre y lo salude con su nombre
    print("-----EJERCICIO 2-----")
    nombreUsuario = input("Ingrese su nombre: ")
    print("Hola", nombreUsuario)

elif ejercicio == 3:
    # 12. Ingresar dos numero y realizar toddas las operaciones aritmeticas
    print("-----EJERCICIO 3-----")
    primerNumero = int(input("Ingrese el primer número: "))
    segundoNumero = int(input("Ingrese el segundo número: "))
    print("La suma de los dos número es: ", primerNumero + segundoNumero)
    print("La resta de los dos número es: ", primerNumero - segundoNumero)
    print("El producto de los dos número es: ", primerNumero * segundoNumero)
    print("El cociente de los dos número es: ", primerNumero / segundoNumero)
    print("La potencia del primer número, elevado al segundo es: ",
          primerNumero ** segundoNumero)
    print("La raiz enesima del primer número, en relación al segundo es: ",
          primerNumero ** (1/segundoNumero))

elif ejercicio == 4:
    # 18. Hallar la potencia de cualquier numero
    print("-----EJERCICIO 4-----")
    numeroBase = int(input("Ingrese un numero (x) para obtener su potencia: "))
    numeroPotencia = int(input("Ingrese la potencia (y) del número: "))
    print("El valor de x^y es: ", (numeroBase**numeroPotencia))

elif ejercicio == 5:
    # 30. Resuelva la siguiente ecuacion y = (-b+(b²+c)^1/2)/2a
    print("-----EJERCICIO 5-----")
    valorA = int(input("Ingrese el valor de a: "))
    valorB = int(input("Ingrese el valor de b: "))
    valorC = int(input("Ingrese el valor de c: "))
    print("El valor de y es:", (-valorB + (valorB*valorB + valorC)**(1/2))/(2*valorA))

else:
    print ("El numero seleccionado es incorrecto.")

