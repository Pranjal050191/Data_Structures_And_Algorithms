def firstRecurring(array1) -> int:
    calc_set = set()
    for i in range(len(array1)):
        if (array1[i] in calc_set):
            return array1[i]
        else:
            calc_set.add(array1[i])
    else:
        return 0
array1 = [2,5,1,2,3,5,1,2,4]
array2 = [2,3,4,5]
array3 = [2,1,1,2,3,5,1,2,4]
array4 = [2,5,5,2]
array5 = [2,1,3,4,6,7,1,4,3,7]
print(f'{firstRecurring(array4)}')
#to print 2 in case of [2,5,5,2] instead of 5

def firstRecurring2(array1) -> int:
    for i in range(len(array1)):
        for j in range(i+1,len(array1)):
            if array1[i] == array1[j]:
                return array1[i]
    return 0
print(f'{firstRecurring2(array5)}')