squareNumbers = [] 

for i in range(1,100+1,1): 

    #print(i**2) 

    if ((i**2) % 3 == 0): 

        squareNumbers.append(i**2) 

print(squareNumbers) 

###########
### ANS ###
###########

print([x**2 for x in range(1,100+1) if x**2 % 3 == 0])
