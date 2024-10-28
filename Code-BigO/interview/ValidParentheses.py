# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid(s: str) -> bool:
    flag1 = 0
    flag2= 0
    flag3 = 0
    nums = [1]
    for i in range(len(s)):
        if s[i] == '(':
            flag1 = flag1 + 1
            nums.append(s[i])
        elif s[i]==')':
            flag1 = flag1 - 1
            if not (nums.pop() == '('):
                return False
        elif(s[i] == '['):
            flag2 = flag2 + 1
            nums.append(s[i])
        elif s[i]==']':
            flag2 = flag2 - 1
            if not (nums.pop() == '['):
                return False
        elif(s[i] == '{'):
            flag3 = flag3 + 1
            nums.append(s[i])
        elif s[i]=='}':
            flag3 = flag3 - 1
            if not (nums.pop() == '{'):
                return False
    if (flag1 == 0) and (flag2 ==0) and flag3 ==0:
        return True
    else:
        return False
s="]"
print(isValid(s))