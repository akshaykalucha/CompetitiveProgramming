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

arr = list(map(int, input().split()))
output = [0]*len(arr)
st = []

for i in range(len(arr)):
    while len(st)!=0:
        if arr[i] > arr[st[-1]]:
            output[st[-1]] = i
            st.pop()
        else:
            break
    st.append(i)
while len(st)!=0:
    output[st[-1]] = -1
    st.pop()
for i in range(len(arr)):
    if output[i]==-1:
        print(-1, end=" ")
    else:
        print(arr[output[i]], end=" ")