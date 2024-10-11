# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

def trailingZeroes(n: int) -> int:
    def factorial(n:int):
        if (n <=2):
            return n
        return n * factorial(n-1)
    a = factorial(n)
    ans = str(a)
    counter = 0
    if(len(ans)>1):
        for i in range(len(ans)-1,-1,-1):
            if(ans[i] == '0'):
                counter = counter + 1
            else:
                return counter
    else:
        return counter

print(trailingZeroes(15))