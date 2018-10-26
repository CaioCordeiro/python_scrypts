print('insira os lados do triangulo')
    l1 = float(input('Lado 1 : '))
    l2 = float(input('Lado 2 : '))
    l3 = float(input('Lado 3 : '))

    if l1!=l2 and l2!=l3 and l1!=l3:
        print('Esse triangulo e escaleno')

    else:
        if ( l1 == l2 and l2!=l3 ) or ( l2==l3 and l1!=l3 ) or (l1 == l3 and l3 != l2) :
            print('Esse triangulo e Isosceles')
        else:
            if l1 == l2 and l2 == l3:
                print('Esse triangulo e Equilatero')
        
