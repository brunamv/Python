p1 = float(input('Digite o valor do primeiro produto: '))
p2 = float(input('Digite o valor do segundo produto: '))
p3 = float(input('Digite o valor do terceiro produto: '))
p4 = float(input('Digite o valor do quarto produto: '))
p5 = float(input('Digite o valor do quinto produto: '))

valorprod = p1 + p2 + p3 + p4 + p5
pgto = float(input('Digite o valor do pagamento: '))

troco = pgto - valorprod
print('O seu troco é: ', troco)