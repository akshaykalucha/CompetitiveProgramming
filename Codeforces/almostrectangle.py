# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')
in1 = lambda : int(input())
in2 = lambda : list(map(int, input().split()))
 
for i in range(in1()):
    n = in1()
    grid = []
    for i in range(n):
        grid.append([*input()])
 
    mark = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                mark.append([i, j])
 
    if mark[0][0] == mark[1][0]:
        d = abs(mark[0][1] - mark[1][1])
        grid[(mark[0][0] + d) % n][mark[0][1]] = '*'
        grid[(mark[1][0] + d) % n][mark[1][1]] = '*'
    elif mark[0][1] == mark[1][1]:
        d = abs(mark[0][0] - mark[1][0])
        grid[mark[0][0]][(mark[0][1] + d) % n] = '*'
        grid[mark[1][0]][(mark[1][1] + d) % n] = '*'
    else:
        grid[mark[0][0]][mark[1][1]] = '*'
        grid[mark[1][0]][mark[0][1]] = '*'
    
    for row in grid:
        print(*row, sep='')