boysNo = input("Enter the number of boys: ")
girlsNo = input("Enter the number of girls: ")
totalNo = int(boysNo) + int(girlsNo)
boysPercentage = round(int(boysNo) / totalNo * 100)
girlsPercentage = round(int(girlsNo) / totalNo * 100)
print(f"Boys: {boysPercentage}%")
print(f"Girls: {girlsPercentage}%")
