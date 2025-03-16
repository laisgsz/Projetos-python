# Chute um numero


#Escreva um programa que ao iniciar gera um valor aleatorio de 1 a 10
#Permita que o usuario chute um numero, diga se for maior ou menor

import random

valor_alt = random.randint(1,10) #funçao para gerar numero aleatorio dentro de um intervalo
acertou = False 

while acertou == False :
    chute = int(input('chute um valor de 1 a 10: '))
    if chute > valor_alt :
        print('Seu numero e maior')
    elif chute < valor_alt :
        print('Seu numero e menor')
    elif chute == valor_alt:
        acertou = True
        print('voce acertou')
   