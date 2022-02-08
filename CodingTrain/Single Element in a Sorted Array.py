Approach 1: (Optimised) Brute Force
There are a few ways to brute force a solution. One way is to count the number of times each element appears in the array, and then return the value with a counter of 1.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            if count == 1:
                return num
        return -1  # this will never be reached
		# return Counter(nums).most_common()[-1][0]  # one-liner, but TC O(nlogn)
TC: O(2n) ~ O(n), since we loop through the array twice.
SC: O(n), since we used a dictionary / Counter object.

Another way is to check if each element has been seen before in the array. This method is intrinsically highly optimised since we know that duplicate elements are adjacent to each other.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        val, seen = -1, True
        for num in nums:
            if val == num:
                seen = True
            elif seen:
                val = num
                seen = False
            else:
                return val
        return -1  # this will never be reached
TC: O(n), since we only loop through the array once.
SC: O(1), since no additional data structures are used.

We can further optimise this method by abusing the adjacency of the duplicate elements: checking elements pairwise for equality.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1, 2):  # pairwise comparison
            if nums[i] != nums[i+1]:  # found the single element
                return nums[i]
        return nums[-1]  # the last element is the single element
