# crie um programa que recebe um numero e imprimi o fatorial

num = int(input('Digite um numero'))

if num > 0:
    fatorial = 1  # começa em 1

# numeroinicial, numero final, + para considerar o numero final
for item in range(1, num + 1):
    fatorial *= item
    print(fatorial)


'''
result fatorial 

    1*1
    1 * 2 = 2
    2 * 3 = 6
    6 * 4 = 24
    24 * 5 = 120
    120 * 6 = 720

    '''
