import heapq
n,k=map(int, input().split())
p=list(map(int, input().split()))

tmp = p[:k]
heapq.heapify(tmp)
tmp_ans = heapq.heappop(tmp)
print(tmp_ans)
for i in range(k,n):
    if p[i]>=tmp_ans:
        heapq.heappush(tmp,p[i])
        tmp_ans = heapq.heappop(tmp)
        print(tmp_ans)
    else:
        print(tmp_ans)

import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
que = P[0:K]
print(min(que))
heapq.heapify(que)
for i in range(K,N):
    minima = heapq.heappop(que)
    minima = max(minima,P[i])
    heapq.heappush(que,minima)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que,ans)
