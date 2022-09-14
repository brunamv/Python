n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))


if (n1==n2==n3):
    print('Os números devem ser diferentes um do outro')

if (n1 > n2) and (n1 > n3):
    if(n2 > n3):
        print(n3, n2, n1)
    else: #(n3>n2)
        print(n2, n3, n1)

    if (n2 > n1) and (n2 > n3):
        if(n1 > n3):
            print(n3, n1, n2)
        else: #(n3>n1)
            print(n1, n3, n2)

        if (n3> n1) and (n3 > n2):
            if (n1 > n2):
                print(n2, n1, n3)
            else: #(n2>n1)
                print(n1, n2, n3)