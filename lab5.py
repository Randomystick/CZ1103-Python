'''
Coding Exercise 5a
a) Write a function get_color(color) that takes a string parameter, “color” as the input
and return the integer value of the color entered by the user, based on the code snippet
given on page 2.
 The function checks for valid value entered by the user, in the range from 0 to 255.
 The function returns the valid value entered by the user
 If the user does not enter a valid value after 3 tries, the function will return a default
value of 0
'''

#from sense_hat import SenseHat
from lab5textcolor import get_color
#sense = SenseHat()
#sense.set_rotation(180)

     
#---------------------------------------------------
r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")
msg_color = (r_int, g_int, b_int)
#sense.show_message("I got it!", text_colour=msg_color)
