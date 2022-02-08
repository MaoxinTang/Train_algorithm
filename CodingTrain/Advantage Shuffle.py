class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        order = sorted(range(n), key=lambda x: B[x], reverse=True)
        ans = [0] * n
        A = deque(sorted(A))
        for ix in order:
            ans[ix] = A.pop() if A[-1] > B[ix] else A.popleft()
        return ans