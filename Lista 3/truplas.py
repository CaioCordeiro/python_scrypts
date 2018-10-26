from operator import itemgetter
listaf = []
while True:
    xs = input('')
    if xs == '':
        break
    xs = xs.split(',')
    listaf.append((tuple(xs)))
print(sorted(tuple(listaf), key=itemgetter(0,1,2)))
