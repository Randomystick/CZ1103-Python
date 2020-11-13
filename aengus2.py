#Aengus Leman, [10.11.20 13:28]
#Given a tree (represented using list of list) and an element x,
#write a function find_x that returns the command required to
#extract the element x from the tree.
#If the element x is not present in the tree, return None.
#If multiple instances of the element x can be found in the tree,
#a command that returns any of the instances is acceptable.

#The command should be return as a string type.

#Note: Please use is to test for equivalence for x.

#Aengus Leman, [10.11.20 13:28]
#find_x(5, [1, 3, [5], 3])
#returns
#[1, 3, [5], 3][2][0] as a string

def find_x(numberToFind, treeToTraverse):
    #base case: we only have one element to compare
    #print(type(treeToTraverse))
 
    '''
    if (type(treeToTraverse) is list):
        print("its a list")
        find_x(numberToFind, treeToTraverse[0])
        find_x(numberToFind, treeToTraverse[2])
    elif (type(treeToTraverse) is int):
        print("its an int")
        print("int is", treeToTraverse)
        if treeToTraverse is numberToFind:
            print("found")
    '''

'''
    size = len(treeToTraverse)
    print("size is", size)

    if size == 1:
        #print("test")
        if (treeToTraverse[0] is numberToFind):
            print("found")
    find_x(numberToFind, treeToTraverse[0])
    
    else:
        treeLeft = find_x(numberToFind, treeToTraverse[0])
        treeRight = find_x(numberToFind, treeToTraverse[1])
#'''

find_x(5, [4,5,6])
#find_x(5,[5])
#find_x(5, [1, 3, [5], 3])
#find_x(5, [[[7], 1, [9]], 3, [[8], 2, [4]]])


