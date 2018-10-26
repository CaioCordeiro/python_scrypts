    altura = float(input('Insira sua altura(em metros) : '))
    peso = float(input('Insira seu peso(em Kg) : '))
    IMC = peso/altura**2
    if IMC>25:
        print('Voce está acima do peso')
    else:
        print('Voce não está acima do peso')
