n = int(input())
cc = 0
cap = []
for i in range(n):
    a, b = map(int, input().split())
    cc-=a
    cc+=b
    cap.append(cc)
print(max(cap))