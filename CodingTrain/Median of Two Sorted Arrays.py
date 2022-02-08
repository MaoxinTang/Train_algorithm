class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            brpoint,c1,c2,a,b=0,0,0,0,0
            n= len(nums1)+len(nums2) -2 
            nums1.append(math.inf)
            nums2.append(math.inf)
            brpoint = n//2 
            while brpoint>=-1:
                val1 = nums1[c1]
                val2 = nums2[c2]
                if(val1<val2):
                    a,b = val1,a
                    c1+=1
                else:
                    a,b = val2,a
                    c2+=1
                brpoint-=1
            if(n&1==0):
                return (a+b)/2
            else:
                return a