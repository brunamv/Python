v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))

if (v1 > v2) & (v1> v3):
    print('O maior valor é: ', v1)
elif (v2 > v3):
    print('O maior valor é: ', v2)
else:
    print('O maior valor é: ', v3)