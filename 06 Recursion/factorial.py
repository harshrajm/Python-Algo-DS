

def factorial(num):
    #base case
    if(num <= 1):
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(5))    