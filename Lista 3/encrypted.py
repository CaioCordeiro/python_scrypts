MAX_KEY_SIZE = 26
def getTranslatedMessage(message, key):

     

     translated = ''



     for symbol in message:

         if symbol.isalpha():

             num = ord(symbol)

             num += key



             if symbol.isupper():

                 if num > ord('Z'):

                     num -= 26

                 elif num < ord('A'):

                     num += 26

             elif symbol.islower():

                 if num > ord('z'):

                     num -= 26

                 elif num < ord('a'):

                     num += 26



             translated += chr(num)

         else:

             translated += symbol

     return translated



flag = 0
keyinput = input('')
rot = keyinput.split(' ',1)
keys = rot[0].split('ROT',1)
if keys[0] != '':
    print('Error')
        
else:
    key0 = keys[1]
    ms = rot[1]
    for i in rot[1]:
        if i.isnumeric() == True:
            flag = 1
        else:
            continue
    if (key0.isnumeric() == False) or (int(key0) < 0 or int(key0) > MAX_KEY_SIZE)or(flag == 1):
        print('Error')
        

    else:
        key =int(key0)
        print(getTranslatedMessage(ms, key)) 
        
    


