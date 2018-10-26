dna = input('Insira a cadeia de DNA : ').upper()

    t = len(dna)

    a = 100*(dna.count('A')/t)
    c = 100*(dna.count('C')/t)
    g = 100*(dna.count('G')/t)
    t = 100*(dna.count('T')/t)
    ptotalval = a+c+g+t
    pinv = 100 - ptotalval

    invt = (pinv*t)/100

    print(' A = {}% \n C = {}% \n G = {}% \n T = {}% \n Porcentagem de invalidos : {}% \n Numero de invalidos : {} '.format(a,c,g,t,pinv,invt))




