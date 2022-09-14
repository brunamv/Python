#ok
p1 = float(input('Digite o valor da primeira prova: '))
p2 = float(input('Digite o valor da segunda prova: '))

media = (p1 + 2*p2)/3

if (media>=5):
    print('Sua média é', media, ',você está APROVADO.')
else:
    print('Sua media é', media, ',você está REPROVADO.')