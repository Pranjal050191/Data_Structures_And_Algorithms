#function1 didn't work as expected, it took the sum of next item only.
def function1(array1,sum):
    for i in range(len(array1)-1):
        if(array1[i] + array1[i+1] == sum):
            return print(f'Found pair: + {array1[i]} and {array1[i+1]}')
    else:
        print('Not found')
#This is brute force and most naive one.
def function2(array1,sum):
    for i in range(len(array1)-1):
        # print(f'In i loop {array1[i]}')
        for j in range(i+1,len(array1)):
            # print(f'In j loop {array1[j]}')
            if (array1[i] + array1[j] == sum):
                print(f'Found pair:  {array1[i]} and {array1[j]}')
#This is most powerful funtionality wise and would work even for unsorted array.
def function3(array1,sum):
     calc_set = set()
     for number in array1:
         print(f'Number is {number}')
         x = sum - number
         if number not in calc_set:
             print(f'Adding {x} in {calc_set}')
             calc_set.add(x)
         else:
             return True
     else:
         return False
#This is most optimised for time complexity and would work only for sorted array.     
def function4(array1,sum):
    y = len(array1)-1
    i = 0
    while(y >= i):
        #print(f'first is {array1[i]} second is {array1[y]}')
        if (array1[i] + array1[y] == sum):
            return True
        elif(array1[i] + array1[y] > sum):
            y = y - 1
        elif(array1[i] + array1[y] < sum):
            i = i + 1
    else:
        return False
        
array1 = [1,2,3,4,5,6,7,8,9]
sum = 25
print(f'found pair: {function4(array1,sum)}')
print(5 ** 20000)
    