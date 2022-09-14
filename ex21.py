v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
resp = 0

x= int(input('\nSelecione uma opção: \n1- Multiplicação \n2 - Adição \n3 – Divisão \n4 – Subtração \n5 – Fim de processo, sair do programa \n\nDigite aqui sua opção:'))

if (x==1):
    resp = v1 * v2
    print('O resultado é: ', resp)

if(x==2):
    resp = v1 + v2
    print('O resultado é: ', resp)

if(x==3):
    resp = v1 / v2
    print('O resultado é: ', resp)

if(x==4):
    resp = v1 - v2
    print('O resultado é: ', resp)

if(x==5):
    print('Fim do programa')