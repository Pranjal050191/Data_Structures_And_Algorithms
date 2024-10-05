numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(numbers):
    pointer = 1
    for j in range(len(numbers)-1,0,-1):
        for i in range(len(numbers)-pointer):
            print(f'comparing values: {numbers[i+1], numbers[i]}')
            if (numbers[i+1] < numbers[i]):
                a = numbers[i]
                numbers[i] = numbers [i+1]
                numbers[i+1] = a
                print(f'Value of j is {j} + {numbers}')
        pointer = pointer + 1

bubbleSort(numbers);
print(numbers);