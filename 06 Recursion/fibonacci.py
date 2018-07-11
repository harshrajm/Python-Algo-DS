#starting from 0 print the element in the postion
def fibonacci(num):
    
    if(num <= 1):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
print(fibonacci(8))    