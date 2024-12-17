textFile = open("input.txt")

leftList = []
rightList = []

for x in range(len(textFile)):
    leftList.append(textFile[x][4:])
    rightList.append(textFile[x][:7])
    
sorted = False
while not sorted:
    