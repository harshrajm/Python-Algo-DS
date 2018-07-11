



def bubbleSort(arr):
    
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            print(f" n {n} - k {k}")
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr

print(bubbleSort([2,6,1,5,9,4,3]))    