#from sense_hat import SenseHat
#sense = SenseHat()

#sense.set_rotation(180)

msgColour = [[-1,-1,-1], [-1,-1,-1]] 
ColourList = []
needInt = "Please key in an integer. Discarding previous input..."
i=0
j=0
triesLeft = 3

currentcol = []
currenttype = []
while True:
    if i == 0: currentcol = "RED"
    elif i == 1: currentcol = "GREEN"
    elif i == 2: currentcol = "BLUE"
    if j == 0: currenttype = "TEXT"
    elif j == 1: currenttype = "BACKGROUND"
    outputMsg = "Enter the value of the "+ currentcol + " for "+ currenttype + ". Enter ~~~~ to exit: "
    
    if triesLeft == 0:
        print("You exceed max number of tries")
        break
    
    USERINPUT = input(outputMsg)
    
    if USERINPUT == "~~~~":
        print("Exiting program")
        break
    
    try:
        msgColour[j][i] = int(USERINPUT)
    except ValueError:
        print(needInt)
        triesLeft -= 1
        print("You have", triesLeft, "tries left.")
        continue
    if (msgColour[j][i] > 255 or msgColour[j][i] < 0):
        print("Enter a value between 0 and 255")
        triesLeft -= 1
        print("You have", triesLeft, "tries left.")
        continue
    
    else: #means the number is accepted already
        if i==2: 
            i=0
            j= not j
            print("Current text colour is", msgColour[0])
            print("Current background colour is", msgColour[1])
            if (msgColour[0] == msgColour[1]):
                print("The text and background colour cannot be the same.")
                triesLeft -= 1
                print("You have", triesLeft, "tries left.")

        else: 
            i += 1
        continue
