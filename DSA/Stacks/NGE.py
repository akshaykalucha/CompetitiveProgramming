#Using O(n^2)

# arrMain = [4,5,2,25,7,8]
# arr = []

# for i in range(len(arrMain)):
#     currEl = arrMain[i]
#     Flag = True
#     for j in range(i, len(arrMain)):
#         if arrMain[j] > currEl:
#             arr.append(arrMain[j])
#             Flag = False
#             break
#     if Flag == True:
#         arr.append(-1)
# print(arr)

# Using stack

# arr = list(map(int, input().split()))
# output = [0]*len(arr)
# st = []

# for i in range(len(arr)):
#     while len(st)!=0:
#         if arr[i] > arr[st[-1]]:
#             output[st[-1]] = i
#             st.pop()
#         else:
#             break
#     st.append(i)

# while len(st)!=0:
#     output[st[-1]] = -1
#     st.pop()
# for i in range(len(arr)):
#     if output[i]==-1:
#         print(-1, end=" ")
#     else:
#         print(arr[output[i]], end=" ")


# NGE using iterating list from back

# arr = [5,2,3,7,1,8,6,566,44,21,56]
# stack = []
# output = [0]*len(arr)
# i = len(arr)-1
# while i >= 0:
#     while len(stack)!=0:
#         if arr[stack[-1]]>arr[i]:
#             output[i]=stack[-1]
#             break
#         else:
#             stack.pop()
#     stack.append(i)
#     i-=1


# for i in range(len(output)):
#     if output[i]==0:
#         output[i] = -1
#     else:
#         output[i]=arr[output[i]]
# print(output)


# NGE using asbolute value but reverse

arr = [5,2,3,7,1,8,6,566,44,21,56]
stack = []
output = []
i = len(arr)-1
while i>=0:
    while len(stack)!=0:
        if stack[-1]<arr[i]:
            stack.pop()
        else:
            break
    if len(stack)==0:
        output.append(-1)
    else:
        output.append(stack[-1])
    stack.append(arr[i])
    i-=1
print(output[::-1])