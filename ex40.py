#ok
#neste exercicio o usuário não deverá digitar nada, é somente a lógica do ex.

a = -1
b = 1
c = 1
r = a + b + c

for i in range(1,21,1):
    print(r)
    c = b
    b = a
    a = r
    r = a+b+c