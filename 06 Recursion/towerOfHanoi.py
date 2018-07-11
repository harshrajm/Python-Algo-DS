

def towerOfHanoi(num,frm,aux,to):
    if num == 1:
        print (f"{frm} -> {to}")
    else:
        towerOfHanoi(num-1,frm,to,aux)
        towerOfHanoi(1,frm,aux,to)
        towerOfHanoi(num-1,aux,frm,to)
        
        
towerOfHanoi(3,"a","b","c")        