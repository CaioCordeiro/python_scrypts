c = 0

b = 0

e = 0

d = 0

def direcao(x):
	global c
	global b
	global e
	global d
	xs = x.split()
	if xs[0] == 'CIMA':
		c += int(xs[1])
	if xs[0] == 'BAIXO':
		b += int(xs[1])
	if xs[0] == 'ESQUERDA':
		e += int(xs[1])
	if xs[0] == 'DIREITA':
		d += int(xs[1])


while True:
	x = input().upper()
	if x == '':
		break
	else:
		direcao(x)
		continue

z = ((c - b)**2 + (d - e)**2)**(1/2)
z = round(z)
print(z)

