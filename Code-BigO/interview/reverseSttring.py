# def reverseString(s: list[str]) -> None:
#     srt = []
#     for i in range(len(s)-1,-1,-1):
#         srt.append(s[i])
#     for i in range(len(srt)):
#         print(srt[i],end = '')

# def reverseString(s: list[str]):
#     if (len(s) ==0):
#         return s
#     else:
#         return reverseString(s[1:]) + s[0]

def reverseString(self,s: list[str]) -> None:
    i = 0
    j = len(s)-1
    while(j>i):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i = i+1
        j =j-1

s = ["h","e","l","l","o"]
# input_string = "yoyo master" //It didnt work
reverseString(s)
print(s)