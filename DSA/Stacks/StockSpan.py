import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

arr = list(map(int, input().split()))
stack = []
output = [0]*len(arr)

# for i in range(len(arr)):
#     while len(stack)!=0:
#         if arr[stack[-1]] > arr[i]:
#             output[i]=stack[-1]
#             break
#         else:
#             stack.pop()
#     if len(stack)==0:
#         output[i]=-1
#     stack.append(i)
    
# for i in range(len(output)):
#     if output[i]==-1:
#         output[i]=i+1
#     else:
#         output[i] = i-output[i]
# print(output)

# Traversing from back of array

i = len(arr)-1

while i >= 0:
    while len(stack)!=0:
        if arr[stack[-1]] < arr[i]:
            output[stack[-1]] = i
            stack.pop()
        else:
            break

    stack.append(i)
    i-=1

while len(stack)!=0:
    output[stack[-1]] = -1
    stack.pop()
    
for i in range(len(output)):
    if output[i]==-1:
        output[i]=i+1
    else:
        output[i] = i - output[i]
print(output)