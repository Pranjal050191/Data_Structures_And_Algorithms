def mergeSortedArrays(array1,array2):
    array3 = []
    x = len(array1)
    y = len(array2)
    a = 0
    b = 0
    while(a < x and b < y):
        if(array1[a] > array2[b]):
            array3.append(array2[b])
            b = b + 1
        else:
            array3.append(array1[a])
            a = a + 1
    while a < x:
        array3.append(array1[a])
        a = a + 1
    while b < y:
        array3.append(array2[b])
        b = b + 1 
    return array3
array1 = [1,4,7,8]
array2 = [2,3,4,7,8,9]
print(f'{mergeSortedArrays(array1,array2)}')
        


