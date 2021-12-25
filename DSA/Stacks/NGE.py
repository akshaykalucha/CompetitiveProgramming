# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


#Using O(n^2)

arr = [3,7,8,7,4,1,3,2,8]
output = [0]*len(arr)
st = []
i = len(arr)-1
while i>=0:
    while len(st)!=0:
        if arr[i]>arr[st[-1]]:
            output[st[-1]]=i
            st.pop()
        else:
            break
    st.append(i)
    i-=1
while len(st)!=0:
    output[st[-1]]=-1
    st.pop()
print(output)
print(arr)

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
# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i]=arr[output[i]]

# print(output)


# NGE using iterating list from back

# arr = list(map(int, input().split()))
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
#     if len(stack) == 0:
#         output[i]=-1
#     stack.append(i)
#     i-=1

# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i]=arr[output[i]]
# print(output)


# NGE using asbolute value but reverse

# arr = list(map(int, input().split()))
# stack = []
# output = []
# i = len(arr)-1
# while i>=0:
#     while len(stack)!=0:
#         if stack[-1]<arr[i]:
#             stack.pop()
#         else:
#             break
#     if len(stack)==0:
#         output.append(-1)
#     else:
#         output.append(stack[-1])
#     stack.append(arr[i])
#     i-=1
# print(output[::-1])

# NGE to left using absolute value

# arr = list(map(int, input().split()))
# stack = []
# output = []

# for i in range(len(arr)):
#     while len(stack)!=0:
#         if stack[-1]<arr[i]:
#             stack.pop()
#         else:
#             output.append(stack[-1])
#             break
#     if len(stack)==0:
#         output.append(-1)
#     stack.append(arr[i])
# print(output)

#NGE left using index

# arr = list(map(int, input().split()))
# stack = []
# output = [0]*len(arr)

# for i in range(len(arr)):
#     while len(stack)!=0:
#         if arr[i]>arr[stack[-1]]:
#             stack.pop()
#         else:
#             output[i]=stack[-1]
#             break
#     if len(stack)==0:
#         output[i]=-1
#     stack.append(i)


# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i]=arr[output[i]]
# print(output)

# NGE to left iterating from last

# arr = list(map(int, input().split()))
# output = [0]*len(arr)
# stack = []
# i = len(arr)-1

# while i>=0:
#     while len(stack) != 0:
#         if arr[stack[-1]] < arr[i]:
#             output[stack[-1]] = i
#             stack.pop()
#         else:
#             break
#     stack.append(i)
#     i-=1
# while len(stack)!=0:
#     output[stack[-1]] = -1
#     stack.pop()
# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i] = arr[output[i]]
# print(output)


# Nearest Smaller to left

# arr = list(map(int, input().split()))
# output = [0]*len(arr)
# stack = []

# for i in range(len(arr)):
#     while len(stack)!=0:
#         if arr[stack[-1]]<arr[i]:
#             output[i] = stack[-1]
#             break
#         else:
#             stack.pop()
#     if len(stack)==0:
#         output[i] = -1
#     stack.append(i)

# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i]=arr[output[i]]
# print(output)

# Nearest smaller element to left from backward

# arr = list(map(int, input().split()))
# stack=[]
# output = [0]*len(arr)
# i = len(arr)-1

# while i>=0:
#     while len(stack)!=0:
#         if arr[stack[-1]]>arr[i]:
#             output[stack[-1]] = i
#             stack.pop()
#         else:
#             break
#     stack.append(i)
#     i-=1
# while len(stack)!=0:
#     output[stack[-1]] = -1
#     stack.pop()

# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i]=arr[output[i]]
# print(output)

# Nearest smaller element to right

# arr = list(map(int, input().split()))
# stack = []
# output = [0]*len(arr)

# for i in range(len(arr)):
#     while len(stack)!=0:
#         if arr[stack[-1]] > arr[i]:
#             output[stack[-1]] = i
#             stack.pop()
#         else:
#             break
#     stack.append(i)
# while len(stack)!=0:
#     output[stack[-1]] = -1
#     stack.pop()

# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i]=arr[output[i]]
# print(output)

# Nearest smaller element to right, trabersing from end

# arr = list(map(int, input().split()))
# stack = []
# output = [0]*len(arr)

# i = len(arr)-1
# while i>=0:
#     while len(stack)!=0:
#         if arr[stack[-1]]<arr[i]:
#             output[i] = stack[-1]
#             break
#         else:
#             stack.pop()
#     if len(stack)==0:
#         output[i]=-1
#     stack.append(i)
#     i-=1
# for i in range(len(output)):
#     if output[i]!=-1:
#         output[i]=arr[output[i]]
# print(output)