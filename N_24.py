print("Algoritmo que determine la menor cantidad de billetes de cada denominacion")

d=int(input("Digita la cantidad de dinero: "))

d1=int(d/100000)
d2=d-(d1*100000)
d3=int(d2/50000)
d4=d2-(d3*50000)
d5=int(d4/20000)
d6=d4-(d5*20000)
d7=int(d6/10000)
d8=d6-(d7*10000)
d9=int(d8/5000)
d10=d8-(d9*5000)
d11=int(d10/2000)
d12=d10-(d11*2000)
d13=int(d12/1000)
d14=d12-(d13*1000)

print(str(d1) + " billetes de 100mil pesos")
print(str(d3) + " billetes de 50mil pesos")
print(str(d5) + " billetes de 20mil pesos")
print(str(d7) + " billetes de 10mil pesos")
print(str(d9) + " billetes de 5mil pesos")
print(str(d11) + " billetes de 2mil pesos")
print(str(d13) + " billetes de mil pesos")
print("Final del programa")

