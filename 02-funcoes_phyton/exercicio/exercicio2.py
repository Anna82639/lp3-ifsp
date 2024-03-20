 #Programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.

print("Programa Calcula Media \n")

a = float(input("Digite o primeiro numero: "))

b = float(input("Digite o segundo numero: "))

c = float(input("Digite o terceiro numero: "))

media = (a + b + c) / 3

media = round(media, 2) 

print("Media =", media)