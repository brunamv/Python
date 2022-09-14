v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))


if (v1==v2 or v1==v3 or v2==v3):
    print('Os números são iguais, digite novamente!')

if (v1 > v2) and (v1 > v3):
    if (v2 > v3):
        print(v1, v2, v3)
    else: #(v3>v2)
        print(v1, v3, v2)

    if (v2 > v1) and (v2 > v3):
        if(v1 > v3):
            print(v2, v1, v3)
        else: #(v3 > v1)
            print(v2, v3, v1)

        if (v3 > v1) and (v3 > v2):
            if(v1 > v2):
                print(v3, v1, v2)
            else: #(v2>v1)
                print(v3, v2, v1)