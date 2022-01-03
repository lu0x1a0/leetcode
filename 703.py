from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        sortnum = sorted(nums)
        self.k = k
        self.useful = sortnum
    def add(self, val: int) -> int:
        #print("--------")
        #print(self.useful)

        if len(self.useful):
            for i,x in enumerate(self.useful):
                if val<=x:
                    if i>0:
                        self.useful = self.useful[:i]+[val]+self.useful[i:]
                        break
                    else:
                        self.useful = [val]+self.useful[i:]
                        break
                elif i == (len(self.useful)-1):
                    self.useful.append(val)
                    break
        else:
            self.useful = [val]
        #trimming:
        if len(self.useful)>self.k:
            self.useful = self.useful[-self.k:]
        #print(self.useful)
        if len(self.useful)<self.k:
            return self.useful[0]
        else:
            return self.useful[-self.k]
S = KthLargest(1, [])
print(S.add(-3))
print(S.add(-2))
print(S.add(-4))
print(S.add(0))
print(S.add(4))


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)