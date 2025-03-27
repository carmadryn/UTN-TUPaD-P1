#1 -Crear un programa que imprima por pantalla "Hola Mundo!"
#print = ("Hola Mundo!")

#2 -Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
#nombre = input("Ingrese su nombre: ")
#print (f"Hola {nombre}!")

#3 - Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

#nombre = input("como se llama?")
#apellido = input("cual es su apellido?")
#edad = input("cual es su edad?")
#residencia = input("Donde vive?")

#print (f"Soy {nombre}  , tengo  {edad} y vivo en{residencia}")

# 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
#radio= float (input ("Digame el radio de un circulo "))
#pi=3.14
#area= pi * radio ** 2
#perimetro = 2 * pi * radio

#print(f"El area del circulo es:  {area}, y su perimetro es {perimetro}") 


# 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

#segundos= int (input("Dime una cantidad de segundos"))
#hora=segundos/3600

#print(f"La cantidad de segundos convertidas en horas son : {hora}")

#6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
#numero=int(input("dime un numero"))
#uno= numero*1
#dos=numero*2
#tres= numero*3
#cuatro= numero*4
#cinco=numero*5
#seis= numero*6
#siete= numero*7
#ocho=numero*8
#nueve= numero*9

#print (f"La tabla de multriplicar del {numero} es : {numero}x1={uno}, {numero}x2={dos}, {numero}x3={tres}, {numero}x4={cuatro},{numero}x5={cinco}, {numero}x6={seis}, {numero}x7={siete}, {numero}x8={ocho}, {numero}x9={nueve}")

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
#numero1= int(input("escriba un numero diferente al 0 ="))
#numero2= int(input("ahora escriba otro numero ="))

#suma= numero1+numero2
#div= numero1/numero2
#mult= numero1*numero2
#resta= numero1 - numero2

#print (f"La suma de los dos numeros es = {suma}, la resta= {resta}, la division = {div} y la multiplicacion = {mult}")

#8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

#peso=int(input("cual es su peso? "))
#altura= float(input("cual es su altura?"))

#imc= peso/(altura*altura)
#print (f"su indice de masa corporal es de {imc}")

#9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
#celsius= int(input("que temperatura hace en celsius?"))
#fahre= ((celsius*9)/5) + 32

#print (f"la temperatura en fahrenheit es = {fahre}")

#10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1= int(input("escriba un numero entero "))
num2= int(input("escriba otro "))
num3= int(input("y por ultimo uno mas "))

promedio= (num1+num2+num3)/3
print (f"El promedio de los tres numeros es = {promedio}")
