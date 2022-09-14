#sintaxe correta, devo verificar se o calculo está certo.
v0 = float(input('Digite a velocidade: '))
a = float(input('Digite a aceleração do carro: '))::::
t = float(input('Digite o tempo do percurso: '))

v = v0 + a * t

if (v <= 40):
    print('Veículo muito lento')
elif (v <= 60):
    print('Velocidade permitida')
elif (v <= 80):
    print('Velocidade de cruzeiro')
elif (v <= 120):
    print('Veiculo rápido')
else:
    print('Veiculo muito rapido')