# cook your dish here
t = int(input('No of test cases: '))
N = []
Q = []
M = []
K = []
for i in range(t):
    n,q = map(int,input().split())
    N.append(n)
    Q.append(q)
    for j in range(n):
        medals = list(map(int,input().split()))
        M.append(medals)
    for j in range(q):
        k = int(input())
        K.append(k)
G = []
S = []
B = []
for i in range(len(M)):
    G.append(M[i][0])
    S.append(M[i][1])
    B.append(M[i][2])
#G_max = max(G)
for i in range(len(K)):
    count = 0
    #count2 = 0 
    #count3 = 0
    #count4 = 0
    for j in range(len(M)):
        if j != 0 and K[i] != 0:
            if G[j]-K[i] < G[0]:
                count += 1
            
            if G[j]-K[i] == G[0]:
                #B[j] = B[j] + K[i]
                if S[0] > S[j]:
                    #count2 += 1
                    count += 1

                elif S[0] == S[j]:
                    r = B[j] + K[i]
                    if B[0] > r:
                        #count3 += 1
                        count += 1

        if j != 0 and K[i] == 0:
            if G[0] > G[j]:
                count += 1
            elif G[0] == G[j]:
                if S[0] > S[j]:
                    count += 1
                elif S[0] == S[j]:
                    if B[0] > B[j]:
                        count += 1
                    elif B[0] == B[j]:
                        count += 1
                


    
    for f in range(1,len(M)-count+1):
        if len(M)-count == f:
            print(f)
            break