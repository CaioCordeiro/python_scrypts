senha = input('')
senha = senha.split(',')
senhasok = []
def alpha(snh):
	for x in snh :
		if x.isalpha() == True :
			return True

def special(snh):
	carac1 = '@'
	carac2 = '#'
	carac3 = '$'
	for x in snh :
		if x == carac1 or x== carac2 or x== carac3:
			return True

def maiusculo(snh):
	for x in snh:
		if x.isupper() == True:
			return True

def minusculo(snh):
	for x in snh :
		if x.islower() == True :
			return True
def num(snh):
	for x in snh :
		if x.isnumeric() == True :
			return True
def tamanho(snh):
	lenx = len(snh)
	if lenx >= 6 and lenx <= 12 :
		return True


def final(snh):
	if alpha(snh) and num(snh) and special(snh) and maiusculo(snh) and minusculo(snh) and tamanho(snh) :
		return True

for i in senha :
	if final(i) == True :
		senhasok.append(i)
	else:
		continue
print(','.join(senhasok))


