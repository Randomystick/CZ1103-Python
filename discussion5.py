'''
1. Generate a list of four random numbers 0-9, no repeat
2. game not won 
3. while game not won: 
    get user input of 4 digits 
    for each user input digit i: 
    for each element j in list: 
        if same value: 
            confirm 1b(cow)
        check if position same. if yes, confirm 1a (bull)
    if a = 4, game won, else print a and b 
'''

# The digits must be all different!!
from random import randint


def getNumber():
    number = []
    i = 0
    while (i < 4):
        randNo = randint(0,9)
        if randNo not in number:
            number.append(randNo)
            i += 1
        else:
            continue
    return number
#x = getNumber()
#print(x)

def getUserNumber():
    while True:
        try:
            userNumber = input("Guess the number: ")
            userNumber = int(userNumber)
            break
        except ValueError:
            print("Input a number.")
            continue
    '''TODO: check that input has 4 digits'''
    '''also need to return a list with the 4 ints, not the 4 ints directly'''
    return userNumber


lmao = getUserNumber()
for i in lmao:
    print(lmao)
#def numberOfAB():
    

'''
gameWon = 0
attempts = 0
NUMBERTOGUESS = getNumber()
while not (gameWon):
    NUMBERGUESSED = getUserNumber()
    AB = numberOfAB(NUMBERTOGUESS, NUMBERGUESSED)
    attempts++
    if AB[0] == 4:
        print("You r winner")
        print("Attempts:")
        gameWon = 1
    else:
        print("There are", AB[0], "A (bull) and ", AB[1],"B (cow).")
'''
