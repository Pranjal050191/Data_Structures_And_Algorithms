# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits
#  it has (also known as the Hamming weight).
def hammingWeight(n: int) -> int:
    nums = bin(n)
    st = nums[2:]
    counter = 0
    for i in range(len(st)):
        if (st[i] == '1'):
            counter = counter + 1
    return counter
print(hammingWeight(2147483645))