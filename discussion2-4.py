
# Data validation
while True:
    try:
        width = int(input("Enter width of pattern: "))
    except ValueError:
        print("Please key in an integer.")
        continue
    else:
        break

# Create list of values 1 to width+1 then back to 1.
starsList = list(range(1,width+1)) + list(range(width-1,0,-1))

# for i in range(len(starsList)) == for i in starsList

# for numbers 1,2,3,4,5...
for noOfStars in starsList:
    # print the asterick for that number of times
    print("*" * noOfStars)


'''
# for numbers 1,2,3,4,5...
for noOfStars in starsList:
    #iterate over them to print
    for i in range(noOfStars):
        print("*", end="")
    print("")
    
'''

###########
### ANS ###
###########

width_str = input("Enter pattern width: ")
width = int(width_str)
#display first 5 rows
for count in range(1, width+1):
    print(count * "*")
    '''
    for j in range(i):
        print("*", end="")
    print()
    '''
    
#display last 4 rows
for count in range(width-1, 0, -1):
    print(count * "*")
    '''
    for j in range(i):
        print("*", end="")
    print()
    '''

###########
### ANS ###
###########

width = int(input("Pls enter pattern width: "))
for i in range(width*2):
    count=i
    if i > width:
        count = width * 2 - count
    for j in range(count):
        print("*", end="")
    print()
