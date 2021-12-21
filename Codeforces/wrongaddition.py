import sys
sys.stdout = open('DSA/Stacks/output.txt', 'w')
sys.stdin = open('DSA/Stacks/input.txt', 'r')

def find(a,s):
    i = len(s) -1
    j = len(a) -1
    
    res = ''
    c = 0
    while i >-1 and j >-1:
        if int(s[i]) >= int(a[j]) and int(s[i]) - int(a[j]) <10:
            res += str(int(s[i]) - int(a[j]))
            i -= 1
            j -= 1
        elif i > 0 and int(s[i-1:i+1]) > int(a[j]) and int(s[i-1:i+1]) - int(a[j]) <10:
            res += str(int(s[i-1:i+1]) - int(a[j]))
            i -= 2
            j -= 1
            c += 1
        else:
            return -1
    if i >= j:
        return int(s[:i+1] + res[::-1])
    else:
        return -1
            
 
r = int(input())
res = []
for i in range(r):
    arr = input().split()
    res.append(find(arr[0], arr[1]))
    
for i in res:
    print(i)