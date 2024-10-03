def fibonacciRecurrsion(number):
    if (number > 1):
        return fibonacciRecurrsion(number-1) + fibonacciRecurrsion(number-2)
    elif (number == 0):
        return 0
    elif (number == 1):
        return 1

def fibonacciIteration(number):
    b = 1
    s = 0
    a = 0
    if (number ==1):
        return 1
    elif (number == 0):
        return 0
    else:
        for i in range(1,number):
            s = b + a
            a = b
            b = s
    return s

#print(fibonacciRecurrsion(50)) # Takes much more time
print(fibonacciIteration(50)) # Takes very less time compare to recurrsion