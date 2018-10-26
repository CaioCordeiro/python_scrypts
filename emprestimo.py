vc = float(input('Qual o valor da casa? '))
    sal = float(input('Qual o seu salario? '))
    anos = float(input('Em quantos anos voce pretende pagar? '))

    meses = anos*12
    prestmen = vc/meses
    pm = (sal*30)/100

    if prestmen>pm :
        print('Seu emprestimo não foi aprovado')
    else:
        print ('Seu emprestimo foi aprovado')

