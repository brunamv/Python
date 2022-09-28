p = float(input('Digite o peso :'))
a = float(input('Digite a altura :'))

imc = p/(a*a)

if (imc > 25):
    print('Você está acima do peso!')
else:
    print('Você está abaixo do peso!')