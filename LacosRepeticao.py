#Laços de Repetição - maneiras de executar o mesmo comando varias vezes
#Listas


for palavra in range(1,4):
    print('carregando')

'''
for item in coleçao:
comandos

range - criar listas no python
'''

for item in range (1,20):
    print(item)


#range - vai ate o penultimo numero, exclui o ultimo

for item in range (1, 21, 2):
    print(item)

#for item in coleçao (numinicio, numfinal, pulos)

#listas
nomes = ['Lais', 'Joao', 'Lucas', 'Cami', 'Bela', 'Luiz']

for nome in nomes:
    print(nome)

#imprimi todos os nomes



#usando for para imprimir valor de 1 a n

num = int(input('digite o valor maximo:'))

for number in range (1, num + 1): #num + 1 é para incluir o valor maximo, pois desconsidera o numero maximo
    print(number)

#Vai gerarvalorese 0 a n

