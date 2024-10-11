# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.
def isPowerOfThree(n: int) -> bool:
    i = 0
    temp = 0
    while(temp < n):
        temp = pow(3,i)
        if (temp == n):
            return True
        i = i +1
    return False
        

print(isPowerOfThree(1))