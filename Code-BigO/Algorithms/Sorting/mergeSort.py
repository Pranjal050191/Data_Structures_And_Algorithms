def divide(array,si,ei):
    # O (log n)
    if(si >= ei ):
        return array
    mid = int(si + (ei-si) /2)
    print(f'Pranjal: {si},{mid},{ei}')
    divide(array,si,mid)
    divide(array,mid+1,ei)
    conquer(array,si,mid,ei)
 
def conquer(array,si,mid,ei):
    #O(n)
    default = None
    merged = [default] * (ei-si+1)
    idx1 = si
    idx2 = mid+1
    x = 0
    j = si
    while(idx1 <=mid) and (idx2 <= ei):
        if(array[idx1] <= array[idx2]):
            merged[x] = array[idx1]
            x = x +1
            idx1 = idx1 + 1
        else:
            merged[x] = array[idx2]
            x = x + 1
            idx2 = idx2 + 1
    while(idx1<=mid):
        merged[x] = array[idx1]
        x = x +1
        idx1 = idx1 + 1
    while(idx2<=ei):
        merged[x] = array[idx2]
        x = x + 1
        idx2 = idx2 + 1
    for i in range(len(merged)):
        array[j] = merged[i]
        j = j +1

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
n = len(numbers)
divide(numbers,0,n-1)
print(numbers)
#O n log(n)