import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
 
for i in range(0, q):
    x = int(input())
    index = bisect.bisect_left(a, x)
    print(n-index)