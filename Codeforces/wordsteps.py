s = input()
ans =0
pre = 'a'
for l in s:
    ans +=min (abs(ord(l)-ord(pre)),26-abs((ord(l)-ord(pre))))
    pre = l
print(ans)