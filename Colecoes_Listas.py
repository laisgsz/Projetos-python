#Coleções - armazenar itens em uma lista

#listas sao mutaveis, podem armax strings, boolean, int, decimal
precos = [20,50,200] 
         # 0, 1, 2

#indice e o addres da informaçao dentro da lista

print(precos[0])
#result: 20

print(precos.index(200))
#funçao para descobrir o valor do indice do meu item na minha coleção

diversidades = ['Lais', 21, True]

for div in diversidades:
    print(div)


 #print(diversidades[0])

idades = [ 20, 40, 60, 60, 20]
total =  0
for id in idades:
    total = total + id
    print(total)

#laço se repete, vai guardando informaçao na memoria


