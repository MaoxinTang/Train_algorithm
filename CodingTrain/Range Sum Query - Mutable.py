class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.sum = sum(nums)

    def update(self, index: int, val: int):
        self.sum += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int):
        if right + 1 - left > len(self.nums) // 2:
            return self.sum - sum(self.nums[:left]) - sum(self.nums[right + 1:])
        return sum(self.nums[left:right + 1])