#Meu primeiro projeto python

print('hello world')

#Variaveis

vel_internet = 10 #int
print(vel_internet)

name = 'Liz' #string

name_course = "Lógica" #aspas simples ou duplas

nota_movie = 8.5 #float 

esta_aberto = True  #1 ou 0
#exemplo de uso: Um sistema que libera a compra de ingressos em um determinado horario, quando chegar aquele horario, true.


x = 2
y = 5

#potenciaçao
print(x ** y) #same as 2*2*2*2*2

#resto da divisao
print(x % y)

print(x // y)
#arredonda para o numero inteiro mais proximo

# x += 3 is the same x = x + 3 

# x -= 3 is the same x = x - 3 

# x *= 3 is the same x = x * 3

# x /= 3 = x = x / 3

# x **= 3 is the same x = x ** 3

salario_mensal = input('Qual e o seu salario mensal ')

horas = input('quantas horas trabalha por mes')

div = int(salario_mensal) / int(horas) #convertendo pra int
print(div)


#Condicionais

#if, elif, else

trabalho_finished = True
if trabalho_finished == True :
    print('Bora sair')
else: print('Nao posso sair\n')

estou_livre = False
if (estou_livre == True):
    print('Ok, posos ajudar')
else : print('Peça ao meu irmao\n')

num_atrasos = 2
if ( num_atrasos >= 3):
    print("voce esta suspenso")
elif (num_atrasos == 1):
    print('voce atrasou 1 vez, caso tome mais 2 faltas, esta suspenso')
elif(num_atrasos == 2):
    print('atrasou 2 vezes, entre')
else: print('pode entrar')


#comparando numeros 

num1 = input('Digite o primeiro valor1: ')
num2 = input('Digite o segundo valor: ')
num3 = input('digite o terceiro valor: ')

if int(num1) > int(num2) and int(num1) > int(num3) :
    print('numero 1 é maior')
elif int(num2) > int(num1) and int(num2) > int(num3):
    print('numero 2 é maior')
elif int(num3) > int(num1) and int(num3) > int(num2):
    print ('numero 3 e maior')


