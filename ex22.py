#ok
d = int(input('Selecione sua opção: \n1 – Triângulo \n2 – Quadrado \n3 – Retângulo \n4 – Círculo \n5 – Fim de processo \n Sua opção é: '))

if (d!= (1) and (2) and (3) and (4) and (5)):
    print('Opção inválida!')

if (d ==1):
    print('Área do triângulo:')
    b= int(input('Digite o valor da base: '))
    a= int(input('Digite o valor da altura: '))
    area= b*a/2
    print('A area do triangulo, é: ', area)

if(d==2):
    print('Área do quadrado:')
    a = int(input('Digite o valor da aresta: '))
    area = a*a
    print('A area do quadrado é: ', area)

if(d==3):
    print('Área do retangulo')
    b = int(input('Digite o valor da base: '))
    a = int(input('Digite o valor da altura: '))
    area = b*a
    print('A área do retângulo é: ', area)

if(d==4):
    print('Área do círculo:')
    r = int(input('Digite o valor do raio: '))
    area = 3.1416 * (r**2)
    print('A área do circulo é: ', area)

if(d==5):
    print('Final do programa!')