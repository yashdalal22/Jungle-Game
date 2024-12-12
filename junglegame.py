
print('                       JUNGLE GAME                     ')
print("Once upon a time a man is driving through the jugle suddenly his car crashed into a stone then he get's up and started running")
print('press 1 for left and 2 for right')
a = int(input('enter a number'))
if a == 1:
    print("a lion started chasing him then suddenly")
    a = int(input('press 1 for left and 2 for right'))
    if a==1:
        print('lion eats him')
        print("GAME OVER")
    elif a==2:
        print("he beat the lion till lion dies")
        print('OP MAN ','then he started running again' )
        a = int(input('press 1 for left and 2 for right'))
        if a==1:
            print("then lion's wife kill the man")
            print('GAME OVER')
        elif a==2:
            print("lion's son eats him")
            print("GAME OVER")
elif a ==2:
    print("and jumped on the lion")
    a = int(input('press 1 for left and 2 for right'))
    if a == 1:
        print("both lion and man became good friend's ")
        print("but after few seconds lion eat's the man")
        print("GAME OVER")
    elif a ==2:
        print("lion invite's the man for party")
        print("press 1 for left and 2 for right")
        a = int(input('press 1 for left and 2 for right'))
        if a == 1:
            print("lion's wife eat's the man")
            print("GAME OVER")
        elif a==2:
            print("man shot's the lion in head after an argument")
            print("victory")
else:
    print("choose 1 or 2")