
def shellSort(arr):
    
    sublistcount = len(arr)//2
    
    while sublistcount>0:
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)

        print(f"gap is {sublistcount}")
        print(f"arr -> {arr}")
        sublistcount = sublistcount//2
    
    return arr
   
        
def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        
        currentValue = arr[i]
        position = i
        
        while position >= gap and arr[position-gap] > currentValue:
            arr[position] = arr[position-gap]
            position = position - gap
            
        arr[position] = currentValue
    return arr    
print(shellSort([55,3,2,5,6,75,4]))        