n1 = float(input('Digite um numero : '))
    n2 = float(input('Digite outro numero : '))
    n3 = float(input('Digite outro numero : '))
    n4 = float(input('Digite outro numero : '))
    n5 = float(input('Digite outro numero : '))

    if n1>=n2 and n1>=n3 and n1>=n4 and n1>=n5 :
        maior = n1
        print('O maior numero e {} '.format(maior))
    else :
        if n2>=n1 and n2>=n3 and n2>=n4 and n2>=n5 :
            maior = n2
            print('O maior numero e {} '.format(maior))
        else:
            if  n3>=n1 and n3>=n2 and n1>=n4 and n3>=n5 :
                maior = n3
                print('O maior numero e {} '.format(maior))
            else:
                if n4>=n1 and n4>=n2 and n4>=n3 and n4>=n5 :
                    maior = n4
                    print('O maior numero e {} '.format(maior))
                else:
                    if n5>=n1 and n5>=n3 and n5>=n4 and n5>=n2 :
                        maior = n5
                        print('O maior numero e {} '.format(maior))
    if n1<=n2 and n1<=n3 and n1<=n4 and n1<=n5 :
        menor = n1
        print('O menor numero e {} '.format(menor))
    else :
        if n2<=n1 and n2<=n3 and n2<=n4 and n2<=n5 :
            menor = n2
            print('O menor numero e {} '.format(menor))
        else:
            if  n3<=n1 and n3<=n2 and n3<=n4 and n3<=n5 :
                menor = n3
                print('O menor numero e {} '.format(menor))
            else:
                if n4<=n1 and n4<=n2 and n4<=n3 and n4<=n5 :
                    menor = n4
                    print('O menor numero e {} '.format(menor))
                else:
                    if n5<=n1 and n5<=n3 and n5<=n4 and n5<=n2 :
                        menor = n5
                        print('O menor numero e {} '.format(menor))

