

def insertionSort(arr):
    
    for i in range(1,len(arr)):
        
        currentVal = arr[i]
        position = i
        
        while position > 0 and arr[position-1] > currentVal:
            
            arr[position] = arr[position-1]
            position = position - 1
        
        arr[position] = currentVal
    return arr


print(insertionSort([55,3,2,5,6,75,4]))