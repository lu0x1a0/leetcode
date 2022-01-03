from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = nums[0] if nums[0] > nums[1] else nums[1]
        max2 = nums[1] if nums[0] > nums[1] else nums[0]
        q = [max1,max2]
        for i, x in enumerate(nums):
            if i >= 2:
                if x>q[1]:
                    if x>q[0]:
                        q[1] = q[0]
                        q[0] = x
                    else:
                        q[1] = x
        return (q[1]-1)*(q[0]-1)

print(Solution().maxProduct([3,7]))