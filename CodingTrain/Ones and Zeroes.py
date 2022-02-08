class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0,0,0)}
        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            part_dp = set()
            for z, o ,v in dp:
                if zeros + z <= m and ones + o <= n:
                    part_dp.add((zeros + z, ones + o ,v + 1))
            dp |= part_dp
        return max(v for _, _, v in dp)