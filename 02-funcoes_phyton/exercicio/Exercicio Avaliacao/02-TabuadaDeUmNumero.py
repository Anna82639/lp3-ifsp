# Tabuada de um número 

numero = int(input("Digite um número para exibir a tabuada: "))


print("Tabuada de", numero, ":")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
