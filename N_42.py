print("Cantidad de digitos que tiene un numero")

n=int(input("Digita un numero: "))
cont=0

while n>=1:
	n=n/10
	cont+=1

print("El numero tiene " + str(cont) + " digitos")
print("Final del programa")

