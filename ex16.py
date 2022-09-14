#ok
c1 = int(input('Digite o valor do cateto: '))
c2 = int(input('Digite o valor de outro cateto: '))
h = int(input('Digite o valor da hipotenusa: '))

if (h*h == (c1*c1)+(c2*c2)):
    print('Este é um triângulo retângulo.')
else:
    print('Este não é um triângulo retângulo.')
