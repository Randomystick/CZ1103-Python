list1 = [561,651,641,651,268,651,841,561,841561]
list2 = [851,684156,4894,8,4,48,4,5698,46,52]

#key-value

gradeDict = {
}

avgScore1 = avgScore2 = 0

for i in list1:
    gradeDict[i] = 1
    avgScore1 += i

for i in list2:
    gradeDict[i] = 2
    avgScore2 += i

avgScore1 = avgScore1 / len(list1)
avgScore2 = avgScore2 / len(list2)

if avgScore1 > avgScore2:
    higherAvg = 1
else:
    higherAvg = 2


maxKey = max(gradeDict.keys()) #max score

print("Highest max score is from class", gradeDict.get(maxKey))
print("Highest average score is from class", higherAvg)


###########
### ANS ###
###########

avg1 = sum(list1) / len(list1)
avg2 = sum(list2) / len(list2)
if max(list1) > max(list2):
    maxNum = 1
else:
    maxNum = 2
if (avg1 > avg2):
    maxAvg = 1
else:
    maxAvg = 2
print('Highest avg from:', maxAvg)
print('Highest score from:', maxNum)
