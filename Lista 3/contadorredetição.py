sentenca = input('')
words = sentenca.split()
result = []  
for i in words:
    result.append("{}:{}".format(i,words.count(i)))
result = list(set(result))
result = sorted(result)

for i in result:
    print(i)
