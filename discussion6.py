# To represent the negative infinity
NEG_INFINITY = float("-inf")


# To represent the positive infinity
INFINITY = float("inf")


############################################################
# functionality: to print a binary tree
# input:
#   t: the binary tree to be printed
#   level: the level of the root node
# output: None

def printTree(t, level):
    if len(t) == 1:     # base case 1: leave node
        print("  " * level, end="")
        print(t[0])
    elif len(t) == 0:   # base case 2: empty node
        print("")
    else:               # recursive step
        printTree(t[2], level + 1)
        print("  " * level, end="")
        print(t[1])
        printTree(t[0], level + 1)


############################################################
# functionality: to obtain the number of nodes in a binary tree
# input:
#   t: the target binary tree
# output: the number of nodes in t

def numOfNodes(t):
    if len(t) == 1:     # base case 1: leave node
        return 1
    elif len(t) == 0:   # base case 2: empty node
        return 0
    else:               # recursive step
        numLeft = numOfNodes(t[0])
        numRight = numOfNodes(t[2])
        return numLeft + numRight + 1

############################################################
# functionality: to obtain the minimum value of nodes in a binary tree
# input:
#   t: the target binary tree
# output: the minimum value of nodes in t

def minNode(t):
    if len(t) == 1:     # base case 1: leave node
        return t[0]
    elif len(t) == 0:   # base case 2: empty node
        return INFINITY
    else:               # recursive step
        leftMin = minNode(t[0])
        rightMin = minNode(t[2])

        return min(leftMin,t[1],rightMin)


############################################################
# functionality: to obtain the maximum value of nodes in a binary tree
# input:
#   t: the target binary tree
# output: the maximum value of nodes in t

def maxNode(t):
    if len(t) == 1:     # base case 1: leave node
        return t[0]
    elif len(t) == 0:   # base case 2: empty node
        return NEG_INFINITY
    else:               # recursive step
        leftMax = maxNode(t[0])
        rightMax = maxNode(t[2])
        
        return max(leftMax, t[1], rightMax)


############################################################
# functionality: to obtain the sum of node values in a binary tree
# input:
#   t: the target binary tree
# output: the sum of node values in t

def sumNodes(t):
    if len(t) == 1:     # base case 1: leave node
        return t[0]
    elif len(t) == 0:   # base case 2: empty node
        return 0
    else:               # recursive step
        leftSum = sumNodes(t[0])
        rightSum = sumNodes(t[2])

        return t[1] + leftSum + rightSum


############################################################
# functionality: to obtain the mirrored tree of a binary tree
# input:
#   t: the target binary tree
# output: the mirrored tree of t

def mirrorTree(t):
    if len(t) == 1:     # base case 1: leave node
        return t
    elif len(t) == 0:   # base case 2: empty node
        return t
    else:               # recursive step
        parent = t[1]
        leftTree = mirrorTree(t[0])
        rightTree = mirrorTree(t[2])
        
        return [rightTree, parent, leftTree]


##############################################################
# main program to test the above functions

tree = [[[7],13,[]], 3, [[8],2,[4]]]

printTree(tree, 0)

print("#nodes: {}".format(numOfNodes(tree)))

print("minValue: {}".format(minNode(tree)))

print("maxValue: {}".format(maxNode(tree)))

print("sum: {}".format(sumNodes(tree)))

mirroredTree = mirrorTree(tree)

printTree(mirroredTree, 0)
