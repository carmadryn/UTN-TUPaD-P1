#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
#edad= int (input ("Que eedad tienes?"))

#if edad >18:
#    print ("eres mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.    
#notaAlumno= float(input("Cual es tu nota ? "))
#if notaAlumno >= 6:
#    print ("Aprobado")
#else:
#    print("desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

#numero=int (input("Ingrese un numero par "))
#if numero % 2 == 0: 
#    print ("Ha ingresado un numero par")
#else:
#    print ("Por favor, ingreso un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
#edad=int (input("Que edad tienes? "))

#if edad   < 12:
#    print ("Nino/a")
#elif edad >= 12 and edad < 18:
#    print ("Adolescente")
#elif edad >=18 and edad  <30:
#    print ("adulto joven")
#elif edad >=30:
#    print ("adulto")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
#contrasena = input ("escriba una contrasena de 8 a 14 caracteres ")
#len cuenta la cantidad de items, caracteres
#if len(contrasena)>8 and len (contrasena) <14:
#    print ("Ha ingresado una contraseña correcta")
#else:
#    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
#from statistics import mode, median, mean 


#import random
#from statistics import mode, median, mean

# Generar una lista de 50 números aleatorios entre 1 y 100
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, la mediana y la media
#moda = mode(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#media = mean(numeros_aleatorios)

# Mostrar los resultados
#print(f"Moda: {moda}")
#print(f"Mediana: {mediana}")
#print(f"Media: {media}")

# Comparar los valores para determinar el sesgo
#if media > mediana > moda:
#    print("Sesgo positivo (a la derecha)")
#elif media < mediana < moda:
#    print("Sesgo negativo (a la izquierda)")
#else:
#    print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 
#solicitar una palabra o frase
#Pido al usuario que ingrese una frase o palabra
#texto = input("Escribí una palabra o frase: ")

# Con la ayuda de AI pude resolverlo
# Verifico si termina en vocal
# Primero, asegurarnos de que el texto no esté vacío para evitar errores
#if texto != "":
#    if texto[-1] in "aeiouAEIOU":
#        texto += "!"  # Agregamos signo de exclamación si termina en vocal

# Paso 3: Imprimimos el resultado
#print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada
# Pedimos al usuario su nombre
#nombre = input("Ingrese su nombre: ")

# Mostramos las opciones
#print("¿Cómo desea ver su nombre?")
#print("1. En mayúsculas")
#print("2. En minúsculas")
#print("3. Con la primera letra en mayúscula")

# Pedimos al usuario que elija una opción
#opcion = input("Ingrese 1, 2 o 3: ")

# Transformamos el nombre según la opción elegida
#if opcion == "1":
#    print("Nombre en mayúsculas:", nombre.upper())
#elif opcion == "2":
#    print("Nombre en minúsculas:", nombre.lower())
#elif opcion == "3":
#    print("Nombre con la primera letra en mayúscula:", nombre.title())
#else:
#    print("Opción no válida.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:

#magnitud= float(input(" Escriba la magnitud del terremoto "))

#if magnitud <3:
#    print ("Muy leve (imperceptible)")
#elif magnitud >=3 and magnitud <4:
#    print ("Leve (ligeramente perceptible).")
#elif magnitud >=4 and magnitud <4:
#    print ("Moderado (sentido por personas, pero generalmente no causa daños).")
#elif magnitud >=5 and magnitud <5:
#    print ("Fuerte (puede causar daños en estructuras débiles).")  
#elif magnitud >=6 and magnitud <7:
#    print ("Muy Fuerte (puede causar daños significativos).")  
#elif magnitud >=7:
#    print ("Extremo (puede causar graves daños a gran escala).")
#else:
#    print ("No es un numero correcto")


# Función para determinar la estación según el hemisferio, mes y día
#def determinar_estacion(hemisferio, mes, dia):
#    if hemisferio == "N":
#        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#            return "Invierno"
#        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#            return "Primavera"
#        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#            return "Verano"
#        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
#            return "Otoño"
#    elif hemisferio == "S":
#        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#            return "Verano"
#        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#            return "Otoño"
#        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#            return "Invierno"
#        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
#            return "Primavera"
#    else:
#        return "Hemisferio no válido"

# Solicitar datos al usuario
#hemisferio = input("¿En qué hemisferio te encontrás? (N/S): ").upper()
#mes = int(input("¿Qué mes es? (1-12): "))
#dia = int(input("¿Qué día es? (1-31): "))

# Obtener y mostrar la estación
#estacion = determinar_estacion(hemisferio, mes, dia)
#print("La estación del año es:", estacion)
