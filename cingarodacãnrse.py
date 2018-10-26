cig = float(input('Quantos cigarros voce fuma por dias ? '))
mintp = cig*10
hrtp = mintp//60
diatp = hrtp//24
hrp = hrtp%24
minp = mintp%60
print('Voce perdeu {} dias {} horas e {} min de vida \n Pare de fumar , faz mal'.format(diatp,hrp,minp))
    
