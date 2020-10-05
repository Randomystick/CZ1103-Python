# the data structure to serve as a database to use a dictionary
# the key is a tuple (groupName, ID) and the value is the score



dataBase = {}

def inputRecord(dataBase, group, the_id, score):
    groupID = (group,int(the_id))
    dataBase[groupID] = score
    print("Database updated. Now it is ", dataBase)


def query(dataBase, group, the_id):
    '''TODO: try-except KeyError'''
    '''try:
           groupID = (groupID, the_id)
           return dataBase[groupID]
       except KeyError:
           return None
    '''
    '''All code below can be discarded'''
    groupID = (group, the_id)
    #print("groupID is", groupID)
    for i in dataBase:
        #print("i is",i)
        if i == groupID:
            print("Score for index", the_id, "of class", group,"is", dataBase[i])
    

def listGrades(dataBase, group):
    '''TODO: append to list and return it'''
    '''listofGrades = []'''
    for i in dataBase:
        if i[0] == group:
            '''listofGrades.append(database[i])'''
            print(i[1], dataBase[i])
    
    '''return listofGrades'''

def maxGrade(dataBase, group):
    gradeList = []
    for i in dataBase:
        if i[0] == group:
            gradeList.append(dataBase[i])
    '''
    gradeList = listGrades(dataBase, group)
    return max(gradeList)
    '''
    print("Max grade is", max(gradeList))
    

'''
def showMsg:
    .....

INPUT = 1
QUERY = 2
LIST = 3
MAX = 4
LISTALLGROUPS = 5
EXIT = 6

option = INPUT

while option != EXIT:
    showMsg()
    option = int(input("Option: "))
    
    if option == INPUT:
        groupName = input("Please input the group name: ")
        sID = int(input("Please input the student id: ")
        score = int(input("Please input the score: ")
        
        inputRecord(grades, groupName, sID, score)
    
    elif option == QUERY:
        group = input("Please input the group name: ")
        sID = int(input("Please input the student id: "))
        
    elif option == LIST:
    
    .........
    
'''

#inputRecord(dataBase, "DD1", 1, 13)
#inputRecord(dataBase, "DD1", 2, 28)
#inputRecord(dataBase, "DD2", 1, 92)
#query(dataBase, "DD1",1)
#listGrades(dataBase, "DD1")
#maxGrade(dataBase, "DD1")

