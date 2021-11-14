a, b = map(int, input().split())
days = min(a,b)
rem = max(a,b)-min(a,b)

if rem%2==0:
    rem = rem//2
else:
    rem = (rem-1)//2
    
print(days, rem)