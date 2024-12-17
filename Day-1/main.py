def sort(array):
    sorted = False
    while not sorted:
        for x in range(len(array)-1):
            if array[x] > array[x+1]:
                temp = array[x]
                array[x] = array[x+1]
                array[x+1] = array[x]
                sorted = True
        if sorted:
            sorted = False
        else:
            sorted = True

textFile = open("Day-1\input.txt")

textArray = []
for x in textFile:
    textArray.append(textFile.readline())
    
print(textArray)
print(len(textArray))

leftList = []
rightList = []

for x in range(len(textArray)):
    leftList.append(textArray[x][:5])
    rightList.append(textArray[x][8:13])
    
sort(leftList)
sort(rightList)