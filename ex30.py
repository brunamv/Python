#ok
pg = float(input('Digite o valor do produto: '))
f = int(input('Digite a forma do pagamento: \n 1- À vista em dinheiro ou cheque, recebe 10% de desconto \n 2-À vista no cartão de crédito, recebe 15% de desconto \n 3-Em duas vezes, preço normal de etiqueta sem juros \n 4-Em quatro vezes, preço normal de etiqueta mais juros de 10% \n Digite aqui: '))

if (f==1):
    total = pg * 90/100
    print('O valor do produto é de: ',total)

if(f==2):
    total = pg * 85/100
    print('O valor do produto é de: ', total)

if(f==3):
    total = pg
    print('O valor do produto é de: ', total)

if(f==4):
    total = pg * 110/100
    print('O valor do produto é de: ', total)