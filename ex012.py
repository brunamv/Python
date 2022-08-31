b = int(input('Digite o valor da base do retângulo: '))
a = int(input('Digite o valor da altura do retângulo: '))

area = b*a

if area > 100:
    print('Terreno grande')
else:
    print('Terreno pequeno')