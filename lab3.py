from sense_hat import SenseHat
sense = SenseHat()

sense.set_rotation(180)

msgColour = [-1,-1,-1]
needInt = "Please key in an integer. Discarding previous input..."

for i in range(3):
    value = []
    while True:
        if i == 0: value = "RED"
        elif i == 1: value = "GREEN"
        elif i == 2: value = "BLUE"
        outputMsg = "Enter the value of the "+ value + " for message: "
        try:
            msgColour[i] = int(input(outputMsg))
        except ValueError:
            print(needInt)
            continue
        if (msgColour[i] > 255 or msgColour[i] < 0):
            print("Enter a value between 0 and 255")
            continue
        else:
            break
#print(msgColour)

while True:
    try:
        msgSpeed = int(input("Now enter the speed value: "))
    except ValueError:
        print(needInt)
    else:
        break

sense.show_message("This is not fun", text_colour = msgColour, scroll_speed = msgSpeed)
