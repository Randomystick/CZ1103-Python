
#--- function get_color() ---------------------------
def get_color(color):
    no_of_try=1
    color_int = -1
    while (no_of_try <= 3):
        color_str=input("Enter the value of the " + color + " color for message (0 to 255):")
        try:
            color_int = int(color_str)
            if not (0 <= color_int <= 255):
                    #invalid colour
                    print("Enter a number between 0 and 255. You have", 3-no_of_try, "tries left.")
                    no_of_try += 1
                    continue
            else:
                break
        except ValueError:
            print("Enter a NUMBER. You have", 3-no_of_try, "tries left.")
            no_of_try += 1 
            continue
    if no_of_try == 4:
        print("Setting default value of 0.")
        return 0
    else:
        return color_int