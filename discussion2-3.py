'''
0 and 1 as starting numbers
add both numbers tgt to get new number
assign current second number as first number
assign new number to second number
print second number
'''

maxVal = 1000

number1 = 0
number2 = 1
print("1", end="")

while (number1+number2) < maxVal:
    numberSum = number1+number2
    number1 = number2
    number2 = numberSum
    print(", ", end="")
    print(number2, end="")


###########
### ANS ###
###########

a = 1
b = 1
while a<1000:
    print(a)
    a, b = b, a+b
