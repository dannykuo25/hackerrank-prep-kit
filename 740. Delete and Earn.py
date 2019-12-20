class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        take = noTake = 0
        prev = None
        # construct the count dictionary
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        # dynamic programming
        for k in sorted(dic):
            # not adjacent
            if k - 1 != prev: 
                noTake, take = max(noTake, take), k * dic[k] + max(noTake, take)
            else: # adjacent
                noTake, take = max(noTake, take), k * dic[k] + noTake
            prev = k
        return max(noTake, take)
            
        