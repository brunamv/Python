#escaleno = todos != 
#isosceles = 2 ==
#equilat = todos == 

a = int(input('Digite o primeiro valor do triângulo: '))
b = int(input('Digite o segundo valor do triângulo: '))
c = int(input('Digite o terceiro valor do triângulo: '))

if ((a+b > c) and (a+c > b) and (b+c > a)):
    print('É um triângulo!')
else:
    print('Não é um triângulo!')

if (a==b) and (a==c):
    print ("Triângulo Equilátero")
elif ((a!=b) and (a!=c) and (b!=c)):
    print ("Triângulo Escaleno")
else:
    print("Triângulo Isósceles")

