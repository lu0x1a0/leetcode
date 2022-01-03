from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]
        #print(stones)    
        sortedstones = sorted(stones)
        if stones[-2] == stones [-1]:
            return self.lastStoneWeight(sortedstones[:-2])
        else:
            #print(stones[-1],stones[-2])
            x = sortedstones[:-2]
            x.append(abs(sortedstones[-1]- sortedstones[-2]))
            return self.lastStoneWeight(x)
print(Solution().lastStoneWeight([3,7,2]))