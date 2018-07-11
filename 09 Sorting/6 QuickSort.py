

def partition(start,end,arr):
    
    pivot = arr[end]
    i = start - 1
    j = start
    print(f"initial {arr}")
    while(j<end):
        print(f"comparing pivot {pivot} with {arr[j]}" ) 
        if arr[j] <= pivot:
            i += 1
            print(f"swapping {arr[j]} and {arr[i]}")
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        print(arr)
            
        j += 1
    i += 1
    temp1 = arr[i]
    arr[i] = pivot
    arr[end] = temp1
    
    return i  

def quickSort(arr):
    quickSortHelper(0,len(arr)-1,arr)
    return arr    
def quickSortHelper(start,end,arr):
    if end>start:
        
        splitPoint = partition(start,end,arr)
        quickSortHelper(start,splitPoint-1,arr)
        quickSortHelper(splitPoint+1,end,arr)
    return arr    
print(quickSort([6,4,7,3,2,56,5]))    