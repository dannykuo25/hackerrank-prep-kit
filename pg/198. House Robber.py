class Solution:
    def rob(self, nums):
        noRob = rob = 0
        for num in nums:
            tmp = rob 
            rob = num + noRob 
            noRob = max(noRob, tmp)
        return max(noRob, rob)
            
        