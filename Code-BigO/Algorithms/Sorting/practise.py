def bubbleSort(numbers):
    pointer = 1
    for i in range (len(numbers)):
        for j in range(len(numbers)-pointer):
            print(f'Comparing values: {numbers[j]} , {numbers[j+1]}')
            if (numbers[j] > numbers[j+1]):
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
        print(numbers)
    pointer = pointer + 1
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# bubbleSort(numbers);
# print(numbers);

def selectionSort(numbers):
    for i in range(len(numbers)):
        lowest = numbers[i]
        k = i
        for j in range(i+1,len(numbers)):
            print(f'Comparing values: {lowest} , {numbers[j]}')
            if (lowest > numbers[j]):
                lowest = numbers[j]
                k = j
        if not(i==k):
            temp = numbers[i]
            numbers[i] = numbers[k]
            numbers[k] = temp
        print(numbers)
# selectionSort(numbers);
# print(numbers);

def insertionSort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            print(f'Comparing numbers: {numbers[j+1]} , {numbers[j]}')
            numbers[j+1] = numbers[j]
            j = j-1
        numbers[j+1] = key
        print(numbers)
# insertionSort(numbers);
# print(numbers);

def mergeSort(numbers,si,ei):
    if(si>=ei):
        return numbers
    mi = int(si + (ei-si)/2)
    print(mi)
    mergeSort(numbers,si,mi)
    mergeSort(numbers,mi+1,ei)
    conquer(numbers,si,mi,ei)

def conquer(numbers,si,mi,ei):
    import copy
    #Create an empty array with given array size
    default = None
    temp_array = [default] * (ei-si+1) # here is the significance of this length. I tried with len(numbers) - 1 as well. Didn't work.
    #Create pointer to two divided array
    idx1 = si
    idx2 = mi+1
    #Create pointer to traverse new temp array and existing array
    x = 0
    j = si
    while(idx1 <=mi) and (idx2 <= ei):
        if(numbers[idx1] <= numbers[idx2]):
            temp_array[x] = numbers[idx1]
            x += 1
            idx1 += 1
        else:
            temp_array[x] = numbers[idx2]
            x += 1
            idx2 += 1
    while(idx1 <=mi):
        temp_array[x] = numbers[idx1]
        x += 1
        idx1 += 1
    while (idx2 <= ei):
        temp_array[x] = numbers[idx2]
        x += 1
        idx2 += 1
    # numbers = copy.deepcopy(temp_array) Deep copy didn't work
    for i in range(len(temp_array)):
        numbers[j] = temp_array[i]
        j = j +1

# mergeSort(numbers,0,len(numbers)-1)
# print(numbers)

def quickSort(array,low,high):
    if(low < high):
        pivot_index = partition(array,low,high)
        quickSort(array,low,pivot_index-1)
        quickSort(array,pivot_index+1,high)

def partition(array,low,high) -> int:
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if (array[j] < pivot):
            i = i+1
            #Swap
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    i = i+1
    temp = array[i]
    array[i] = pivot
    array[high] = temp
    return i # pivot index

quickSort(numbers,0,len(numbers)-1)
print(numbers)
