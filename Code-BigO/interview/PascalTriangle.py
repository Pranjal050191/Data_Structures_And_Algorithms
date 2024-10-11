# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
def generate(numRows: int) -> list[list[int]]:
    # pascal = list(list(int))
    pascal = []
    for i in range(1,numRows+1):
        si = 0
        ei = i - 1
        array1 = list()
        array1.append(1)
        while(si < ei):
            temp_array = pascal[i-2]
            if (si < len(temp_array)-1):
                array1.append(temp_array[si] + temp_array[si+1])
            si = si +1
        if (i > 1):
            array1.append(1)
        pascal.append(array1)
    return pascal

print(generate(1))