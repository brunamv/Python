#ok
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if (n1 > n2):
    print('O segundo valor deve ser maior.')
    n2 = float(input('Digite o segundo valor: '))
    print('Ótimo, agora o segundo valor é maior.')
else:
    print('Ótimo! O segundo valor é maior.')