# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    task = input()
    done = []
    flag = True
    for i in range(n):
        if task[i] not in done:
            done.append(task[i])
        else:
            if done[-1] == task[i]:
                done.append(task[i])
            else:
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")