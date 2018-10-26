salario = float(input('Insira seu salario : '))
    desconto = (salario*11)/100
    if desconto> 318.20:
        desconto2 = 318.20
        print('O valor de desconto e {}'.format(desconto2))
    else:
        print('O valor de desconto e {}'.format(desconto))
