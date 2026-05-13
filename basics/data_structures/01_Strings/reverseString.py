def reverseString(s: str):
    # code here
    res=""
    size=len(s)
    for i in range (1,len(s)+1):
        res+=s[size-i]
    return res

print(reverseString("hello world"))