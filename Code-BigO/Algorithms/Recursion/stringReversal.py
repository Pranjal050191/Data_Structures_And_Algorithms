def reverseString(input_str):
    rvrstr = []
    # print(input_str[2])
    for i in range(len(input_str)-1,-1,-1):
        rvrstr.append(input_str[i])
    print(''.join(rvrstr))

reverseString("yoyo master")

def reverse_string(s):
    # Base case: if the string is empty, return the empty string
    if len(s) == 0:
        return s
    else:
        # Recursive case: reverse the substring and append the first character at the end
        return reverse_string(s[1:]) + s[0]

# Example usage
input_string = "yoyo master"
reversed_string = reverse_string(input_string)
print("Reversed String:", reversed_string)
