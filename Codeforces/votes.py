n = int(input())
for i in range(n):
   t = input().split(" ")
   a = int(t[0])
   b = int(t[1])
   c = int(t[2])
   m = max(a,b,c)
   if(a == b == c):
      a = 1
      b = 1
      c = 1
   elif(a == b == m or b == c == m or c == a == m):
      a = (1, m - a + 1)[a != m]
      b = (1, m - b + 1)[b != m]
      c = (1, m - c + 1)[c != m]
   else:
      a = (0, m - a + 1)[a != m]
      b = (0, m - b + 1)[b != m]
      c = (0, m - c + 1)[c != m]
   print(a,b,c)
