wordList = ['We', 'like', 'Python', 'I', 'like', 'Python',]
print("index for like: ", wordList.index('like'))

'''

def bubbleSort1(alist):
    for passnum in range(len(alist)-1):
        for i in range(len(alist)-passnum-1):   
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        print("pass", passnum+1, ":", alist)

alist = [3,5,8,11,17,20]
bubbleSort1(alist)
print(alist)



def bubbleSort2(alist):
    for passnum in range(len(alist)-1):
        swapped = False
        for i in range(len(alist)-1):   
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                swapped = True
        print("pass", passnum+1, ":", alist)
        if not swapped:
            break;

alist = [3,5,8,11,17,20]
bubbleSort2(alist)
print(alist)
'''
