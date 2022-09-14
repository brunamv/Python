#ok
soma = 0 
#a soma está sendo declarada aqui em cima, para não entrar no looping e ficar sempre zerando a variável soma.

for i in range(1, 11, 1):
    num = int(input('Digite um número maior que zero: '))


    while(num<0):
        print('[ERRO!] Digite números positivos.')
        num = int(input('Digite um número maior que zero: '))

    if (i==1):
        maior = num #num sempre será maior quando i estiver na posição 1, ainda não tem outros parâmetros de comparação.
    elif (num > maior): #elif está vendo se i na posição 2 em diante, é maior do que o primeiro número.
        maior = num


    soma = soma + num

media = soma/10

print('O maior valor é: ',maior)
print('A soma é: ',soma)
print('A média dos valores, é: ',media)