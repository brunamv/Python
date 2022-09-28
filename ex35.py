#ok
valor = int(input('Digite qualquer valor: '))

while (valor < 0):
    print('[ERRO!] Digite um valor maior que zero.')
    valor = int(input('Digite novamente um valor: '))


for i in range(1, 10, 1):
    print(f"{valor} x {i} = {valor*i}")