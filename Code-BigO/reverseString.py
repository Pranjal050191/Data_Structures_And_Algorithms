def reverseString(input):
    if not isinstance(input,str):
        raise ValueError('Input must be string')
    input2 = []
    y = len(input)-1
    while (y >= 0):
        input2.append(input[y])
        y = y - 1
    return ''.join(input2)
print(f'{reverseString("hello my name is Pranjal")}')
string1 = "hello my name is Pranjal"
reversed_words = ' '.join(word[::-1] for word in string1.split()[::-1])
print(reversed_words)

