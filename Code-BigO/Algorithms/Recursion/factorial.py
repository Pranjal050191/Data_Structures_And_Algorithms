def factorialRecursive(number):
    if (number > 1):
        return number * factorialRecursive(number-1)
    elif(number == 1):
        return 1
def factorialIterative(number):
    product = 1
    if (number == 1):
        return product
    for i in range (2,number+1):
        product = product * i
    return product
        
print(factorialRecursive(10))
print(factorialIterative(2))
    