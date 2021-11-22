# import sys
# sys.stdin = open("Codeforces/input.txt", 'r')
# sys.stdout = open("Codeforces/output.txt", 'w')

n = int(input())
ll = list(map(int, input().split()))

def lenOfLongIncSubArr(arr, n):
    m = 1
    l = 1
    for i in range(1, n) :
        if arr[i] > arr[i-1]:
            l =l + 1
        else :
            if m < l:
                m = l
            l = 1
    if m < l :
        m = l      
    return m
print(lenOfLongIncSubArr(ll, n))