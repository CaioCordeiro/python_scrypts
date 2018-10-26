
    dia = int(input('Insira o dia : '))
    mes = int(input('Insira  o mes (em numero) : '))
    ano = int(input('Insira o ano : '))

    dia1 = dia+1

    mes1 = mes+1

    ano1 = ano+1

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 ) and dia < 31 :
            print('{}-{}-{}'.format(dia1,mes,ano))

    else:
            if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia == 31 :
                  print('1-{}-{}'.format(mes1,ano))

            else:
                if mes == 12 and dia == 31:
                    print('1-1-{}'.format(ano1))

                else:
                    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia < 30 :
                        print('{}-{}-{}'.format(dia1,mes,ano))

                    else:
                        if  (ano%400)==0 or ((ano%4)==0 and (ano%100) != 0) and mes == 2 and dia == 29 :
                            print('1-{}-{}'.format(mes1,ano))

                        else:
                            if  (ano%400)!=0 and ((ano%4)!= 0 or (ano%100)==0) and mes == 2 and dia == 28 :
                                print('1-{}-{}'.format(mes1,ano))

                            else:
                                if  (ano%400)==0 or ((ano%4)==0 and (ano%100) != 0) and mes == 2 and dia < 29 :
                                    print('{}-{}-{}'.format(dia1,mes,ano))

                                else:
                                     if (ano%400)!=0 and ((ano%4)!= 0 or (ano%100)==0)  and mes == 2 and dia < 28 :
                                        print('{}-{}-{}'.format(dia1,mes,ano))
                                     else:
                                         if (ano%400)!=0 and ((ano%4)!= 0 or (ano%100)==0) and mes == 2 and dia == 29:
                                             print('Não existe dia 29 , pois o ano não é bissexto')
                             
                            
                        
