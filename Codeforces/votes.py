for _ in range(int(input())):
   a, b, c = map(int, input().split())
   if a == b == c:
      print(a+1, b+1, c+1)
   else:
      m = max(a,b,c)
      if a==b==m or a==c==m or b==c==m:
         if a!=m:
            print(abs(a-m)+1, m+1, m+1)
         elif b!=m:
            print(m+1, abs(b-m)+1, m+1)
         else:
            print(m+1, m+1, abs(c-m)+1)
      else:
         if a==m:
            print(0, abs(b-m)+1, abs(c-m)+1)
         elif b==m:
            print(abs(a-m)+1, 0, abs(c-m)+1)
         else:
            print(abs(a-m)+1, abs(b-m)+1, 0)