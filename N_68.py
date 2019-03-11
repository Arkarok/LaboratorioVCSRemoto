print("Cantidad variable de numeros")

pos=0
neg=0
par=0
imp=0
m8=0
a=int(input("Digita un numero: "))
b=int(input("Digita un otro numero: "))

for num in range(a,b+1):
	if num>0:
		pos+=1
	elif num==0:
		print("Hay un numero neutro")
	else:
		neg+=1

	if num%2==0:
		par+=1
	else:
		imp+=1
	if num%8==0:
		m8+=1

print("Hay " + str(pos) + " numeros positivos")
print("Hay " + str(neg) + " numeros negativos")
print("Hay " + str(par) + " numeros pares")
print("Hay " + str(imp) + " numeros negativos")
print("Hay " + str(m8) + " multiplos de 8")
print("Fin del programa")
