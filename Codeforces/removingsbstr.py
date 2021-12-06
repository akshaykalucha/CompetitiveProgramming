# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    s = list(int(c) for c in input())
    # print(s)
    stack = []
    counts = []
    for i in range(len(s)):
        cc = 0
        if s[i]==0:
            while len(stack)>0:
                cc+=1
                stack.pop()
            counts.append(cc)
        elif s[i]==1:
            stack.append(s[i])
    counts.append(len(stack))
    stack=[]
    pts = 0
    counts.sort(reverse=True)
    for i in range(len(counts)):
        if i%2==0:
            pts+=counts[i]
    print(pts)