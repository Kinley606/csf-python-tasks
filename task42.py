user_name = str(input('enter your name :'))
vowels = ['a','e', 'i', 'o', 'u']
i = 0
while i< len(user_name):
    if user_name[i] in vowels:
        print(True)
        break
    i+= 1
else:
    print('False')


