def quickSort(array,low,high):
    if(low < high):
        pivot_index = partition(array,low,high)
        quickSort(array,low,pivot_index-1)
        quickSort(array,pivot_index+1,high)

def partition(array,low,high) -> int:
    pivot = array[high]
    i = low - 1
    for j in range(low,high,1):
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


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
n = len(numbers)
quickSort(numbers,0,n-1)
print(numbers)