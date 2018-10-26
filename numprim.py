num = int(input('Digite um número'))
d = 0
i = 2
if (num%2== 2) and (num!=2):
    print('Número não é primo')
    
    
while i < num//2:
    mod = num%i
    i = i+1
    if mod == 0:
        d = d+1
        
if d > 0:
    print('numero não é primo')
else:
    print('numero é primo')
    
    
