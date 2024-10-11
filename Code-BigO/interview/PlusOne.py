# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any 
# leading 0's.

# Increment the large integer by one and return the resulting array of digits.
def plusOne(digits: list[int]) -> list[int]:
    l = len(digits)
    carry = 0
    added = 0
    if not(digits[l-1] == 9):
        digits[l-1] = digits[l-1] + 1
        return digits
    else:
        for i in range (l-1,-1,-1):
            if (digits[i] == 9) and ((added == 0) or (carry == 1)):
                digits[i] = 0
                carry = 1
                added = 1
            elif not(digits[i] == 9):
                digits[i] = digits[i] + carry
                carry = 0
        if (carry == 1):
            # array1 = list()
            # array1.append(1)
            # for i in range(l):
            #     array1.append(digits[i])
            # return array1
            return [1] + digits
        else:
            return digits
digits = [9,9]
print(plusOne(digits))