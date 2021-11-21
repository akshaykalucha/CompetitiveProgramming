import sys
sys.stdin = open('Codeforces/input.txt', 'r')
sys.stdout = open('Codeforces/output.txt', 'w')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    count = 0
    
    imp =[]
    
    for element in ll:
        if element%3==0:
            count+=1
        else:
            imp.append(element)
    if count==n:
        print(0)
    else:
        if len(imp)%2!=0:
            print(-1)
        else:
            imp.sort()
            flag = True
            moves = 0
            while flag:
                if len(set(imp)) != len(imp):
                    flag = False
                    break
                if len(imp)==0:
                    break
                for i in range(len(imp)-1):
                    for j in range(i+1, len(imp)):
                        if ((imp[i]-1)%3==0 and (imp[j]+1)%3==0) or ((imp[i]+1)%3==0 and (imp[j]-1)%3==0):
                            moves+=1
                            imp.pop(j)
                            imp.pop(i)
                            break
                        else:
                            if j+1==len(imp):   
                                flag = False
                                break
                    break
            if flag:
                print(moves)
            else:
                print(-1)