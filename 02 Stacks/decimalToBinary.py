stack = []
num = 251

while num >= 1:
    i = num%2
    stack.append(i)
    num = num // 2
    print(f' {i} - {num}')
    
output = ""
#print(stack)
while stack:
    output =  output + str(stack.pop())

print(f'-> {output}')    