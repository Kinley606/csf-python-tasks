user_name= input('enter your name:')
vowels = "a,e,i,o,u"
for i in user_name:
    if i in vowels :
        print (True)
        break
else:
    print(False)