sa0 = float(input('Insira seu salário : '))
por = float(input('Insira insira a porcentagem do aumento(sem o %) : '))

aum = sa0*(por/100)

salF =  sa0 + aum
print('seu salário teve um aumento de {} , passando a ser {}'.format(aum,salF))
