
def selectionSort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        print(f"fillslot {fillslot}")
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
            print(f"positionOfMax {positionOfMax} - locn {location}")
        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp    
    return arr        
print(selectionSort([55,3,2,5,6,75,4]))            