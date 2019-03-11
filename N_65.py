print("Promedio numeros pares e impares")

par=0
impar=0

a=int(input("Digita un numero: "))

for num in range(1,a+1):
	if num%2==0:
		par+=1
	else:
		impar+=1

print("La cantidad de pares es " + str(par))
print("La cantidad de impares es " + str(impar))
print("Final del programa")

