#1 Bubble Sort
def bubble(arr):
    for x in range(len(arr)-1,0,-1):
        for i in range(x):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr
#------------------------------------------------------
#2 Selection Sort
def selectionSort(arr):
    
    for lastPlace in range(len(arr) - 1, 0 , -1):
        max = arr[lastPlace]
        location = lastPlace
        for i in range(lastPlace):
            if arr[i] > max:
                location = i
                max = arr[i]
        temp = arr[lastPlace]
        arr[location] = temp
        arr[lastPlace] = max
    return arr    
   
#------------------------------------------------------          
#3 Insertion Sort
def insertionSort(arr):
    for i in range(1,len(arr)): 
        
        currentValue = arr[i]
        position = i
        
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position = position-1
        arr[position] = currentValue
    return arr    


#------------------------------------------------------
#4 Shell Sort

def shellSort(arr):
    subListCount = len(arr)//2
    while subListCount > 0:
        for start in range(subListCount):
            insertionSortWithGap(arr,start,subListCount)        
        subListCount = subListCount//2
    return arr

def insertionSortWithGap(arr,start,gap):
    for x in range (start+gap,len(arr),gap):
        currentValue = arr[x]
        position = x
        while position >= gap and arr[position-gap] > currentValue:
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position] = currentValue
    return arr    
#------------------------------------------------------
#5 MergeSort


def mergeSort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2 
        leftSide = arr[:mid]
        rightSide = arr[mid:]
    
        mergeSort(leftSide)
        mergeSort(rightSide)
    
        i = 0
        j = 0
        k = 0
    
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                arr[k] = leftSide[i]
                i+=1
            else:
                arr[k] = rightSide[j]
                j+=1
            k+=1    
        
        while i < len(leftSide) and k < len(arr):
            arr[k] = leftSide[i]
            i+=1
            k+=1
            
        while j < len(rightSide) and k < len(arr):
            arr[k] = rightSide[j]
            j+=1
            k+=1
        return arr    
#------------------------------------------------------
#6 QuickSort
def quickSort(arr):
    
    quickSortHelper(0,len(arr)-1,arr)
    return arr

def quickSortHelper(start,end,arr):
    if(end>start):
        midPoint = partition(start,end,arr)
    
        quickSortHelper(start,midPoint-1,arr)
        quickSortHelper(midPoint+1,end,arr)
    
    return arr

def partition(start,end,arr):
    
    pivot = arr[end]
    i= start-1
    j= start
    while (j<end):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j += 1    
    i += 1
    temp1 = arr[i]
    arr[i] = pivot
    arr[end] = temp1
    return i
#print(bubble([6, 4, 7, 3, 2, 56, 5]))
#print(selectionSort([6, 4, 7, 3, 2, 56, 5]))
#print(insertionSort([6, 4, 7, 3, 2, 56, 5]))
print(quickSort([6, 4, 7, 3, 2, 56, 5]))
print(quickSort([6, 4, 7, 3, 2, 56, 5,34,3456,86,23,4,8,32,67,89]))