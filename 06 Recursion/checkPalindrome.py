def checkPalindrome(str):
    
    if(len(str) <= 1):
        return True
    else:
        l = str[:1]
        mid = str[1:len(str)-1]
        r = str[len(str)-1:]
        print(f"l {l} - mid {mid} - r {r}")
        if(l != r):
            return False
        else:
            return checkPalindrome(mid)
        
result = checkPalindrome("malayalam")        
print(result)        