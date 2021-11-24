import sys
sys.stdin = open("Codeforces/input.txt", 'r')
sys.stdout = open("Codeforces/output.txt", 'w')

tot = 0
for _ in range(int(input())):
    n = int(input())
    A = [0]*4
    B = [0]*4
    C = [0]*4
    D = [0]*4
    earn = []
    profit = [0]*4
    for i in range(n):
        mo, ti = map(str, input().split())
        if mo == "A":
            if ti=="12":
                A[0]+=1
            elif ti=="3":
                A[1]+=1
            elif ti=="6":
                A[2]+=1
            else:
                A[3]+=1
        if mo == "B":
            if ti=="12":
                B[0]+=1
            elif ti=="3":
                B[1]+=1
            elif ti=="6":
                B[2]+=1
            else:
                B[3]+=1
        if mo == "C":
            if ti=="12":
                C[0]+=1
            elif ti=="3":
                C[1]+=1
            elif ti=="6":
                C[2]+=1
            else:
                C[3]+=1
        if mo == "D":
            if ti=="12":
                D[0]+=1
            elif ti=="3":
                D[1]+=1
            elif ti=="6":
                D[2]+=1
            else:
                D[3]+=1
    twelve = [A[0], B[0], C[0], D[0]]
    three = [A[1], B[1], C[1], D[1]]
    six = [A[2], B[2], C[2], D[2]]
    nine = [A[3], B[3], C[3], D[3]]
    earn1 = max(twelve)
    if earn1!=0:
        zz = twelve.index(earn1)
        three.pop(zz)
        six.pop(zz)
        nine.pop(zz)      
    earn.append(earn1)
    earn2 = max(three)
    if earn2!=0:
        zz = three.index(earn2)
        six.pop(zz)
        nine.pop(zz)
    earn.append(earn2)
    earn3 = max(six)
    if earn3 != 0:
        zz = six.index(earn3)
        nine.pop(zz)
    earn.append(earn3)
    earn.append(nine[0])
    earn.sort(reverse=True)
    for i in range(len(earn)):
        if earn[i]==0:
            profit[i]-=100
        else:
            if i == 0:
                profit[i]=100*earn[i]
            elif i == 1:
                profit[i]=75*earn[i]
            elif i==2:
                profit[i]=50*earn[i]
            else:
                profit[i]=25*earn[i]
    print(sum(profit))
    tot+=sum(profit)
print(tot)