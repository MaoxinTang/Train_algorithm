class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=(s+e)//2
            if nums[mid]==target:
                if nums[s]<target:
                    s=s+1
                elif nums[s]==target:
                    if nums[e] > target:
                        e=e-1
                    elif nums[e]==target:
                        return [s , e]
                if nums[e]>target:
                    e=e-1

            elif nums[mid]<target:
                s=mid+1
            else:
                e=mid-1

        return [-1,-1]