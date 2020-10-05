###Practical Exercise 4b
##from sense_hat import SenseHat
##sense = SenseHat()
##sense.set_rotation(180)
###sense.show_message("This is fun!")

max_try = 5 #maximun number of trials for erroronous input

#----------------- using while iteration & if else conditional execution -----------------------------
no_of_try = 0  #Number of trial
while no_of_try < max_try:
    no_of_try = no_of_try + 1
    red_str=input("Enter the value of the red color for message:")
    if red_str.isdigit(): #if the string contains digits only
        msg_r_int= int(red_str) # convert it to integer
        if msg_r_int < 256:   # check whether the range is less than 256      
            break  # yes - valid input
        else:
            print("Invalid - value has to be between 0 and 255 (", no_of_try, ")")
    else:
        print("Invalid - use number only (", no_of_try, ")")

if no_of_try == max_try:
    print("You have exceeded the number of trials allowed. Bye!")
    exit()

#----------------------- using for iteration & if else conditional execution --------------------------------
for no_of_try in range(max_try):
    green_str=input("Enter the value of the green color for message:")
    if green_str.isdigit(): #if the string contains digits only
        msg_g_int= int(green_str) # convert it to integer
        if msg_g_int < 256:   # check whether the range is less than 256      
            break  # yes - valid input
        else: 
            print("Value has to be between 0 and 255 (", no_of_try+1, ")")
    else:
        print("Enter number only (", no_of_try+1, ")")

if no_of_try == max_try-1:   #note that the number is one less than the number of trial when using for loop
    print("You have exceeded the number of trials allowed. Bye!")
    exit()

#-------------- using try and except conditional execution -------------------------
no_of_try=0
while no_of_try < max_try:
    msg_b_str=input("Enter the value of the blue color for message:")
    try: 
        int(msg_b_str) #if this return true, it means that the string contains digits only
        if 0<= int(msg_b_str) < 256:   # further check whether the range is less than 256      
           msg_b_int = int(msg_b_str) # yes - valid input
           break  
        else: 
            print("Invalid - value has to be between 0 and 255")
    except ValueError: #false - not digits
        print("Invalid - enter number only")
    no_of_try += 1
    if no_of_try == max_try:
       print("You have exceeded the number of trials allowed. Bye!")
       exit()

#-------------------------------------------------------------------------------------------
msg_color= (msg_r_int,msg_g_int,msg_b_int)
print ('Message Color = ', msg_color)   #for debugging

bg_color=(0,0,0)  #default values
#red_str=input("Enter the value of the red color for background:")
#green_str=input("Enter the value of the green color for background:")
#blue_str=input("Enter the value of the blue color for background:")
#bg_r_int= int(red_str)
#bg_g_int= int(green_str)
#bg_b_int= int(blue_str)
#bg_color= (bg_r_int,bg_g_int,bg_b_int)
print("Background color = ", bg_color)   #for debugging


#-------------- using try and except conditional execution -------------------------
no_of_try=0
while no_of_try < max_try:
    no_of_try += 1
    speed_str=input("Enter the value of the display speed:")
    try: 
        float(speed_str) #if this return true, it means that the string contains floating number
        if (float(speed_str) >= 0.05 and float(speed_str) <= 1):   # check for valide range      
           speed = float(speed_str) # valid input 
           print("Speed = ", speed)  #for debugging
           break  
        else: 
            print("Invalid - value has to be between 0.05 and 1")
    except ValueError:
        print("Invalid - enter number only")

    if no_of_try == max_try:
       print("You have exceeded the number of trials allowed. Bye!")
       exit()

#--------------------------------------------------------------------------------------------

sense.show_message("I got it!", text_colour=msg_color, \
                                back_colour=bg_color,  \
                                scroll_speed=speed)
                                
