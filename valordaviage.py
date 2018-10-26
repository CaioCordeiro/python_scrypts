es = float(input('Insira o valor da estadiado dia5 a 12 para 4 pessoas'))
pi = float(input('Insira o valor da passagem de ida'))
pv = float(input('Insira o valor da passagem de volta'))
ing = float(input('Insira o valo do ingresso'))
a = float(input('Insira a estimativa de alimentação'))

vt = es+pi+pv+ing+a
print('R${:.2f}'.format(vt))
