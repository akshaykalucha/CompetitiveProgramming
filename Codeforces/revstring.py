import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    z = k
    ss = input()
    mystr = ss[:k]
    st = ""
    i=0
    if k%2!=0:
        mid = (k-1)//2
        while True:
            if mid+i>k-1:
                break
            if i==0:
                st+=mystr[mid]
                i+=1
                continue
            else:
                st+=mystr[mid+i]
                st+=mystr[mid-i]
                i+=1
                continue
        print(st+ss[k:])
    else:
        mid = (k//2)
        while True:
            if i==mid:
                st+=mystr[0]
                break
            if mid+i>k-1:
                break
            if mid-i<0:
                break
            if i==0:
                st+=mystr[mid]
                i+=1
                continue
            else:
                st+=mystr[mid-i]
                st+=mystr[mid+i]
                i+=1
                continue
        print(st+ss[k:])
