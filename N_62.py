print("Suma de numeros naturales contenidos entre m y n")

n=int(input("Digita un numero: "))
m=int(input("Digita otro numero: "))

if n<m:
	print("Continuar el programa")
else:
	print("Parar el programa")

suma=0

for num in range(n,m+1):
	suma=num+num

print(suma)
print("Final del programa")

	