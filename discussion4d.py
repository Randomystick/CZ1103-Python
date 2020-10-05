dataBase = {}

def inputRecord(dataBase, group, the_id, score):
    groupID = (group,int(the_id))
    dataBase[groupID] = score
    print("Database updated. Now it is ", dataBase)


def query(dataBase, group, the_id):
    groupID = (group, the_id)
    #print("groupID is", groupID)
    for i in dataBase:
        #print("i is",i)
        if i == groupID:
            print("Score for index", the_id, "of class", group,"is", dataBase[i])


def listGrades(dataBase, group):
    for i in dataBase:
        if i[0] == group:
            print(i[1], dataBase[i])

def maxGrade(dataBase, group):
    gradeList = []
    for i in dataBase:
        if i[0] == group:
            gradeList.append(dataBase[i])
    print("Max grade is", max(gradeList))

'''
inputRecord(dataBase, "DD1", 1, 13)
inputRecord(dataBase, "DD1", 2, 28)
inputRecord(dataBase, "DD2", 1, 92)
query(dataBase, "DD1",1)
listGrades(dataBase, "DD1")
maxGrade(dataBase, "DD1")
'''


''' REJECTED CODE '''
'''
def inputRecord():
    exitCommand = "~~~~"
    plsExit = 0
    while True and not plsExit:
        for i in range(3):
            
            #Get the group name (string)
            if i == 0:
                group = input("type group: ")
                if group == exitCommand:
                    plsExit = 1
                    break

            #Get the id (0-40)
            if i == 1:
                the_id = input("type id: ")
                if the_id == exitCommand:
                    plsExit = 1
                    break
                the_id = int(the_id)
                if not(0<=the_id<=40):
                    print("ID must be between 0 and 40.")
                    continue

                    
            #Get the score (integer)
            if i == 2:
                score = input("type score: ")
                if score == exitCommand:
                    plsExit = 1
                    break
                else:
                    score = int(score)

        if not plsExit:
            groupID = (group,the_id)
            dataBase[groupID] = score
        else:
            pass
    print("Database updated. Now it is ", dataBase)
'''
