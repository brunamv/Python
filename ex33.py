#erro
sexo = input('Digite seu sexo: ')

while (sexo != 'M' and sexo != 'F'):
    print('Digite novamente M ou F!')
    sexo = input('Digite seu sexo: ').upper()

print('Fim do programa!')