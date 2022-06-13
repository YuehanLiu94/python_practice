#Selection sorting
# find the index of minimum value in a list
# can use build-in function min
def find_min_index(List):
    minIndex = 0
    for i in range(1,len(List)):
        if List[i] < List[minIndex]:
            minIndex = i
    return minIndex

def selection_sorting(iList):
    for i in range(0,len(iList)-1):
        if len(iList) <= 1:
            return iList
        elif iList[i] > find_min_index(iList[i+1:]):
            index_min = iList.index(min(iList[i+1:]))
            iList[i], iList[index_min] = iList[index_min], iList[i]
    return iList

list_input = [7,3,5,1,9,4]
print(selection_sorting(list_input))