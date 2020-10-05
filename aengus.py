'''
count_change(amount, kinds_of_coins) which returns the number of ways
to return change for a given amount n.

The change can be returned using coins worth 100 cents, 50 cents,
20 cents, 10 cents, 5 cents or 1 cent.

For example, count_change(5,2) refers to the number of ways
to get 5 cents using only 5-cents and 1-cent coins.
'''

'''
count_change(5,2)
ah shit
maxdmm 5
amt-mx 0
count_change(0,2)
	ah shit
	amt
	return 1
count_change(5,1)
	ah shit
	maxdmm 1
	amt-mx 4
	count(4,1)
		ah shit
		....
		count(0,1)
			ah shit
			amt
			return 1
'''


# DETERMINE THE HIGHEST COIN DENOMINATION YOU CAN RETURN FOR A CERTAIN AMOUNT
def maxDenom(amount, kinds_of_coins):
    #max 100 cent
    if kinds_of_coins == 6 and amount>=100:
        return 100
    
    #max 50 cent
    if kinds_of_coins >= 5 and amount>=50:
        return 50
    
    #max 20 cent
    if kinds_of_coins >= 4 and amount>=20:
        return 20
    
    #max 10 cent
    if kinds_of_coins >= 3 and amount>=10:
        return 10
    
    #max 5 cent
    if kinds_of_coins >= 2 and amount>=5:
        return 5
    
    #max 1 cent
    if kinds_of_coins >= 1 and amount>=1:
        return 1

def count_change(amount, kinds_of_coins):
    #print("ah shit here we go again")

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''' EDGE CASE: either kinds_of_coins was subtracted till it becomes zero   '''
    ''' (see the count_change(amount, kinds_of_coins-1) function)              '''
    ''' OR user keys in zero.                                                  '''
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    if kinds_of_coins == 0:
        #print("koc")
        return 0

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''' BASE CASE: amount already reduced to zero by the else block via        '''
    ''' recursion                                                              '''
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    if amount == 0:
        #print("amt")
        return 1

    ###############################################################################
    #### RECURSIVE STEP: reduce the current amount to zero. This is done by:   ####
    #### 1) Find out the max denom for the current value                       ####
    #### 2) Subtract this max denom from the current value                     ####
    #### 3) Do step 2 recursively until base case is attained, i.e. amt == 0   ####
    #### 4) Steps 1 to 3 will cause one run of the base case's "return 1".     ####
    #### 5) Remember that we need to do steps 1 to 4 for each possible value   ####
    ####    of kinds_of_coins--. Hence recursively call this function for      ####
    ####    kinds_of_coins-1. This will also decompose into the base case.     ####
    #### 6) Return both these functions.                                       ####
    ###############################################################################
    else:
        maxDenomm = maxDenom(amount, kinds_of_coins)
        #print("  maxDenomm", maxDenomm)
        #print("amount-maxDenomm", amount-maxDenomm)            
        return count_change(amount-maxDenomm, kinds_of_coins) + count_change(amount, kinds_of_coins-1)

    

print(count_change(15,3))




