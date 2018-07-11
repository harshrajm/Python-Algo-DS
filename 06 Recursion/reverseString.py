def reverseString(str):
    
    if(len(str) == 1):
        return str
    else:
        x = str[len(str)-1:]
        y = str[:len(str)-1:]
        return x +  reverseString(y)

#x = "qwerty"
#print(x[len(x)-1:])
#print(x[:len(x)-1])
print(reverseString("abcde"))

print(reverseString("hello world"))
print(reverseString("123456789"))
