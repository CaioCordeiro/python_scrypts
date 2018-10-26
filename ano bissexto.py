ano = float(input('Insira um ano : '))

if (ano%4) == 0 or (ano%400) == 0 :
        print('Esse ano é bissexto')
else:
        print('Esse ano nao é bissexto')
