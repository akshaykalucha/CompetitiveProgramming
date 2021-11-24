import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

arr = list(map(int, input().split()))
stack = []
output = [0]*len(arr)

for i in range(len(arr)):
    while len(stack)!=0:
        if arr[stack[-1]] > arr[i]:
            output[i]=stack[-1]
            break
        else:
            stack.pop()
    if len(stack)==0:
        output[i]=-1
    stack.append(i)
    
for i in range(len(output)):
    if output[i]==-1:
        output[i]=i+1
    else:
        output[i] = i-output[i]
print(output)