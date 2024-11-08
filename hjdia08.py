# valores = input().split()
# a = int(valores[0])
# b = int(valores[1])
# c = int(valores[2])

# resultado0 = (a+b+abs(a-b))/(2)
# resultado = (resultado0+c+abs(resultado0-c))/2

# print("{:.0f} eh o maior".format(resultado))

# variavel1 = input().split()
# variavel2 = input().split()

# x1 = float(variavel1[0])
# y1 = float(variavel1[1])
# x2 = float(variavel2[0])
# y2 = float(variavel2[1])

# distancia = ((((x2-x1)**2)+((y2-y1)**2))**0.5)
# print("{:.4f}".format(distancia))


 
# N = int(input())

# horas = N // 3600 
# print(horas)
# resto = N % 3600
# print(resto)
# minutos = resto // 60 
# print(minutos)
# segundos = resto % 60
# print(segundos)

# print(f"{horas}:{minutos}:{segundos}")

# horas = int(input())
# kmh = int(input())
# litros = (kmh * horas) / 12
# print("{:.3f}".format(litros))

N = int(input())
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador5 = 0
contador2 = 0
contador1 = 0
print(N)
while N >= 100:
    N -=100
    contador100 += 1
else:
    pass
while N >= 50:
    N -=50
    contador50 += 1
else:
    pass
while N >= 20:
    N -=20
    contador20 += 1
else:
    pass
while N >= 10:
    N -=10
    contador10+= 1
else:
    pass
while N >= 5:
    N -=5
    contador5 += 1
else:
    pass
while N >= 2:
    N -=2
    contador2 += 1
else:
    pass
while N >= 1:
    N -=1
    contador1 += 1
else:
    pass


print("{0:.0f} nota(s) de R$100,00".format(contador100))
print("{0:.0f} nota(s) de R$50,00".format(contador50))
print("{0:.0f} nota(s) de R$20,00".format(contador20))
print("{0:.0f} nota(s) de R$10,00".format(contador10))
print("{0:.0f} nota(s) de R$5,00".format(contador5))
print("{0:.0f} nota(s) de R$2,00".format(contador2))
print("{0:.0f} nota(s) de R$1,00".format(contador1))

