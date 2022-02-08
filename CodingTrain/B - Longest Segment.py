import math
N = int(input())
X =[]
Y =[]
for i in range(N):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)

maxD = 0
for i in range(N):
  for j in range(i,N):
    d = math.sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
    if maxD < d: maxD =d
    
print(maxD)
     