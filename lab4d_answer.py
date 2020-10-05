#Practical Exercise 5d
from sense_hat import SenseHat
from time import sleep
from random import choice

sense = SenseHat()
r=(255,0,0)
g=(0,255,0)
b=(0,0,255)
w=(200,200,200)
y=(255,255,0)

sense.show_message("Ready")
#c=choice([y,r,g,w])  #choose a color

c = g 

image_pixels =	[b, b, b, b, b, b, b, b,
                 b, b, b, c, b, b, b, b,
                 b, b, c, c, c, b, b, b,
                 b, c, b, c, b, c, b, b,
                 b, b, b, c, b, b, b, b,
                 b, b, b, c, b, b, b, b,
                 b, b, b, c, b, b, b, b,
                 b, b, b, b, b, b, b, b]
                 
angle = 0  # initial angle
score = 0
delay = 2  # initial delay = 2 second

sense.set_rotation(angle)
sense.set_pixels(image_pixels)

keep_looping = True

while keep_looping:

    #---------- select new random angle ----------            
    new_angle = choice([0, 90, 180, 270])
    while new_angle == angle:
        new_angle = choice([0, 90, 180, 270])
    angle=new_angle    
    
    #---------- display ---------------
    sense.set_rotation(angle)
    sense.set_pixels(image_pixels)
    
    sleep(delay)
    delay = delay * 0.95 # reduced delay by 5%
    
    acceleration = sense.get_accelerometer_raw()
    x_raw = acceleration['x']
    y_raw = acceleration['y']
    x_axis = round(x_raw,0)
    y_axis = round(y_raw,0)
    
    #angle = 0, x,y = 0, 1
    #angle = 90, x,y = -1, 0
    #angle = 180, x,y = 0, -1
    #angle = 270, x,y = 1, 0
    #print("x={0}, y={1}".format(x_axis, y_axis)) #debugging
   
    if angle == 0 and y_axis == 1:
        score += 1
    elif angle == 270 and x_axis == 1:
        score += 1
    elif angle == 180 and y_axis == -1:
        score += 1
    elif angle == 90 and x_axis == -1:
        score += 1
    else: #invalid
        keep_looping = False
        for i, item in enumerate(image_pixels):
            if item == g:
                image_pixels[i] = r
        sense.set_pixels(image_pixels)
        print("Your Score = ", score)
        
sleep(0.5)
msg = "Your score = %s" %score
sense.show_message(msg, text_colour = y)
 
