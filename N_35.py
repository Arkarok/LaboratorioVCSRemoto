print("Algoritmo que imrpima el mayor y el menor de tres numeros")

numb1=int(input("Digita el primer numero: "))
print(numb1)
numb2=int(input("Digita el segundo numero: "))
print(numb2)
numb3=int(input("Digita el tercer numero: "))
print(numb3)

if numb1>numb2 and numb2>numb3:
	print("El mayor de tres numeros es " + str(numb1) + " y el menor de tres numeros es " + str(numb3))
elif numb2>numb3 and numb3>numb1:
	print("El mayor de tres numeros es " + str(numb2) + " y el menor de tres numeros es " + str(numb1))
else:
	print("El mayor de tres numeros es " + str(numb3) + " y el menor de tres numeros es " + str(numb2))

print("Final del programa")

# numero 35