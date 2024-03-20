#Jogo de Adivinhação

import random

numero_secreto = random.randint(1, 100)

print("Tente adivinhar um número entre 1 e 100:")


while True:
   
    palpite = int(input("Seu palpite: "))
    
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto:", numero_secreto)
        break  # Encerrando o loop se o palpite estiver correto
    elif palpite < numero_secreto:
        print("O número secreto é maior do que seu palpite. Tente novamente.")
    else:
        print("O número secreto é menor do que seu palpite. Tente novamente.")
