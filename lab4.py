
###############################
###### CODING EXERCISE 5A #####
###############################
'''

from sense_hat import SenseHat
sense = SenseHat()
from random import randint
from time import sleep


fourCOLOURS = []
for i in range(4):
        colour = (randint(0,255),randint(0,255),randint(0,255))
        if colour not in fourCOLOURS:
            fourCOLOURS.append(colour)
#print(fourCOLOURS)

while True:
    for i in range(4):
        xPos = randint(0,7)
        yPos = randint(0,7)
        sense.set_pixel(xPos, yPos, fourCOLOURS[i])
        print(xPos, ",", yPos, ",", fourCOLOURS[i], sep='')
    sleep(1)
    sense.clear()

  
#'''
###############################
###### CODING EXERCISE 5B #####
###############################
'''

from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
from random import randint

y = (255,255,0)
g = (11,11,11)
b = (0,0,0)
image_pixels = [b, b, b, b, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, y, y, y, b, b, b,
                b, y, b, y, b, y, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, b, b, b, b, b]

image_pixels2 = [g if i==y else i for i in image_pixels]

i = 1
while True:
        orientation = 90*randint(0,3)
        sense.set_rotation(orientation)
        if i:
                #print(image_pixels)
                sense.set_pixels(image_pixels)
        if not i:
                #print(image_pixels2)
                sense.set_pixels(image_pixels2)
        i = not i
        sleep(1)
        sense.clear()

#'''
###############################
###### CODING EXERCISE 5C #####
###############################
'''

from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
from random import randint

y = (255,255,0)
b = (0,0,0)
image_pixels = [b, b, b, b, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, y, y, y, b, b, b,
                b, y, b, y, b, y, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, b, b, b, b, b]

while True:
        orientation = 90*randint(0,3)
        sense.set_rotation(orientation)
        rand = (randint(0,255), randint(0,255), randint(0,255))
        #print([rand if i==y else i for i in image_pixels])
        sense.set_pixels([rand if i==y else i for i in image_pixels])
        sleep(1)
        sense.clear()

#'''
###############################
###### CODING EXERCISE 5D #####
###############################
#'''
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
from random import randint
import time


numberOfSuccess = 0

g = (0,255,0)
b = (0,0,0)
green_arroww = [b, b, b, b, b, b, b, b,
                b, b, b, g, b, b, b, b,
                b, b, g, g, g, b, b, b,
                b, g, b, g, b, g, b, b,
                b, b, b, g, b, b, b, b,
                b, b, b, g, b, b, b, b,
                b, b, b, g, b, b, b, b,
                b, b, b, b, b, b, b, b]

red_arrow = [(255,0,0) if i == g else i for i in green_arroww]

correct = 0
hasBeenSet = 0
timePerRound = 1
timeTotal = time.perf_counter() + timePerRound

print("MAKE THE ARROW POINT UP!")

while time.perf_counter() < timeTotal:
    if not hasBeenSet:
        #Obtain random orientation
        orientation = 90*randint(0,3)
        sense.set_rotation(orientation)
        
        #Draw green rectangle
        sense.set_pixels(green_arroww)
        
        hasBeenSet = 1
    
    else:
        #Rotate to get acceleration value right
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        #print(x,y,z)
        if (orientation == 0 and y>0.75):
            correct = 1
        elif (orientation == 90 and x<-0.75):
            correct = 1
        elif (orientation == 180 and y<-0.75):
            correct = 1
        elif (orientation == 270 and x>0.75):
            correct = 1
        # raspberry pi words are normal: y>0.75
        # usb ports are pointing up: x<-0.75
        
    if (correct):
        numberOfSuccess += 1
        timePerRound -= 0.05
        timeTotal += timePerRound
        correct = 0
        hasBeenSet = 0
        print(numberOfSuccess, "successes so far. Showing next arrow...")
        #print(time.perf_counter())
        #print(timeTotal)

#Game lost
sense.set_pixels(red_arrow)
print("Successes: ", numberOfSuccess)
      
#'''
###############################
