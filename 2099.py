from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # early exit:
        if k == len(nums):
            return nums
        # use selection for small n:
        if k<len(nums)/3:
            for i in range(k):
                temp = nums[-1-i]
                localmax = None
                localmaxidx = None
                for j in range(len(nums)-1-i):
                    if localmax is None:
                        localmax = nums[j]
                    else:
                        if nums[j] > localmax:
                            localmax = num[j]
                            localmaxidx = j
                nums[-1-i] = localmax
                nums[j] = temp
            return sortednums[-k:]
        # sort whole thing when large.
        else:
            sortednums = sorted(nums)
            return sortednums[-k:]

    def alt(self):
        if len(nums) == k:
            return nums
        else:
            x =  sorted(enumerate(nums),key = lambda x:x[1])
            # x = [idx, val] sort by val
            subsample = x[-k:]
            out = [z[1] for z in sorted(subsample,key = lambda x:x[0])]
            return out