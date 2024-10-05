numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
def selectionSort(numbers):
    for i in range(len(numbers)):
        lowest = numbers[i]
        k = i
        for j in range(i+1,len(numbers)):
            print(f'Comparing values: {lowest} , : {numbers[j]}')
            if (lowest > numbers[j]):
                lowest = numbers[j]
                k = j
        temp = numbers[i]
        numbers[i] = lowest
        numbers[k] = temp
        print(numbers);
        
selectionSort(numbers);
print(numbers);