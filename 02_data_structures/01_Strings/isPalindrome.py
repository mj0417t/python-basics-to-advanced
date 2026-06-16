def isPalindrome(s):
    #code here
    s=s.lower()
    if s==reverseString(s):
        return True
    else:
        return False
    
def reverseString(s: str):
    # code here
    res=""
    size=len(s)
    for i in range (1,len(s)+1):
        res+=s[size-i]
    return res


print(isPalindrome("geeks"))
print(isPalindrome("teneT"))