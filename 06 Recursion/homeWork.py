def cumulativeSum(num):
    if(num == 1):
        return 1
    else:
        return num + cumulativeSum(num-1)


def sumOfAllDigits(num): 
    if(num < 10):
        return num
    else:
        return num % 10 + sumOfAllDigits(num//10)
    
def word_split(str):
    
    
    
#print(cumulativeSum(5))
#print(cumulativeSum(4))
print(sumOfAllDigits(12315))