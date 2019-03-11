print("Incremento o Decremento de 3 numeros")

a=int(input("Digita un numero: "))
b=int(input("Digita otro numero: "))
c=int(input("Digita otro numero x2: "))

if a<b and b<c:
	print("Los numeros estan aumentando")
elif a<b and b>c:
	print("Los numeros no incrementan ni decrecen")
else:
	print("Los numeros estan decreciendo")

print("Final del programa")

