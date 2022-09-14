#ok
p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))
s = input('Digite seu sexo, (f ou m): ')

imc = p/(a*a)

if (s == 'f'):
    if (imc < 19):
        print('Seu imc está baixo')
    elif (imc < 24):
        print('Seu imc está ideal')
    else:
        print('Seu imc está alto.')
else: 
    if (s == 'm'):
        if (imc < 20):
            print('Seu ims está baixo')
        elif (imc < 25):
            print('Seu imc está ideal')
        else:
            print('Seu imc está alto')