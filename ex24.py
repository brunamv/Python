#ok
n = input('Digite o seu nome: ')
s = input('Digite o seu sexo (f/m): ')
ec = input('Digite o seu estado civil: ')

if ((s == 'f') and (ec == 'casada')):
    print(input('Digite há quanto tempo você está casada: '))
if (s!= 'f') and (ec != 'casada'):
    print('Fim do programa.')