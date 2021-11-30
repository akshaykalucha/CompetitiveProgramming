import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

arr = list(map(int, input().split()))
NSL = [0]*len(arr)
NSR = [0]*len(arr)
stack = []

for i in range(len(arr)):
    while len(stack)!=0:
        if arr[stack[-1]] < arr[i]:
            NSL[i]=stack[-1]
            break
        else:
            stack.pop()
    if len(stack)==0:
        NSL[i]=-1
    stack.append(i)

stack = []

for i in range(len(arr)):
    while len(stack)!=0:
        if arr[i] < arr[stack[-1]]:
            NSR[stack[-1]] = i
            stack.pop()
        else:
            break
    stack.append(i)
while len(stack)!=0:
    NSR[stack[-1]]=-1
    stack.pop()

ar = 0
for i in range(len(arr)):
    rightspan = 0
    leftspan = 0
    if NSL[i]==-1:
        leftspan = i+1
    elif NSL[i]!=-1:
        leftspan = abs(i-NSL[i])
    if NSR[i]==-1:
        rightspan = abs(len(arr)-i)
    elif NSR[i]!=-1:
        rightspan = NSR[i]-i
    area = (leftspan+rightspan-1)*arr[i]
    if area > ar:
        ar = area
print(ar)
print(NSL)
print(NSR)