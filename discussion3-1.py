# Requirements: length at least 10, at least one upper case, at least one lower case, at least one digit 

C_LENGTH = 10 
PASSWORD = input("Enter a strong password: ")  
hasUpper = hasLower = hasDigit = 0 

for i in PASSWORD:  
    if i.isupper():  
        hasUpper = 1 

    elif i.islower():  
        hasLower = 1

    #isdigit's D must be in smallcaps!  
    elif i.isdigit():  
        hasDigit = 1 

if (hasUpper and hasLower and hasDigit and len(PASSWORD) >= C_LENGTH):  
    print("Password is strong enough. Password set.")  
else: 
    print("Password not strong enough. Requires at least one lowercase, one uppercase, one digit and has to be at least 10 characters long.") 
