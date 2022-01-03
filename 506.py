from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        out = [None for x in score]
        rankorder =  [x[0] for x in sorted(enumerate(score),key=lambda x:x[1],reverse=True)]
        print(rankorder)
        
        if len(out) > 0:
            out[rankorder[0]]  = "Gold Medal"
            if len(out) > 1:
                out[rankorder[1]]  = "Silver Medal"
                if len(out) > 2:
                    out[rankorder[2]]  = "Bronze Medal"
                    if len(out) > 3:
                        for i,x in enumerate(rankorder[3:]):
                            out[x] = str(i+3+1)
        return out
print(Solution().findRelativeRanks([10,3,8,9,4]))