
def seq_search(arr,ele):
    
    pos = 0
    found = False
    
    while pos < len(arr):
        if(ele == arr[pos]):
            found = True
            break
        pos += 1 
    return found    
 
print(seq_search([1,2,3,4,5,6],6))

def ordered_seq_search(arr,ele):
    pos = 0
    found = False
    
    if(ele < arr[0] or ele > arr[len(arr)-1]):
        return "False - before while"
    
    while pos < len(arr):    
        if(ele == arr[pos]):
            found = True
            break
        elif(ele < arr[pos]):
            return "False - in while"
        pos += 1 
    return found

print(ordered_seq_search([1,2,3,4,5,6],6))
print(ordered_seq_search([1,2,3,4,5,6],8))
print(ordered_seq_search([1,2,3,4,5,6],0))
print(ordered_seq_search([3,4,5,6,9,10],7))