def binarySearch(arr,ele):
    
    first = 0
    last = len(arr) - 1
    found = False
    while(last >= first and not found):
        mid = (first+last)//2
        #print(f"first {first} - last {last} - mid {mid}")
        #print(f"{arr[mid]}")
        if(arr[mid] == ele):
            found = True
        elif(arr[mid] > ele):
            last = mid-1
        elif(arr[mid] < ele):
            first = mid + 1
    return found

print(binarySearch([1,2,3,4,5,6,7,8,9,10],0))
print(binarySearch([1,2,3,4,5,6,7,8,9,10],7))


def reccBinarySearch(arr,ele,first,last):
    #print(f" arr {arr} - ele {ele} - first {first} - last {last}")
    if(first>last):
        #print(f" first {first} > last {last}")
        return False
    mid = (first + last)//2
    #print(f"mid - {arr[mid]}")
    
    if(arr[mid] == ele):
        return True
    elif(arr[mid] > ele):
        return reccBinarySearch(arr,ele,first,mid-1)
    elif(arr[mid] < ele):
        return reccBinarySearch(arr,ele,mid+1,last)

arr = [1,2,3,4,5,6,7,8,9,10]        
print(reccBinarySearch(arr,11,1,len(arr)-1))
print(reccBinarySearch(arr,11,8,len(arr)-1))