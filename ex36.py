#ok
num = int(input('Digite um valor qualquer: '))

while (num<0):
    print('Digite somente números maiores do que 0!')
    num= int(input('Digite um valor qualquer: ')) #está repetindo pois o número digitado foi <0.

a = int(input('Digite o valor do intervalo: '))
b = int(input('Digite o fim do intervalo: '))

if (a>b):
    print('Por favor, digite novamente.')
    b = int(input('Digite o fim do intervalo: '))    

for i in range (b, a-1, -1): #pede-se para mostrar de forma decrescente
    tab = num * i
    print (num, 'X', i, '=', tab)