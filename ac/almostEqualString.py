class Solution:
    def almostEqualString(self, s, i, j, k, l):
        result = []
        if self.compare(s, i, j, k, l) == True:
            result.append("SIMILAR")
            return result
        result.append("DIFFERENT")
        return result
    
    def compare(self, s, i, j, k, l):
        if j-i != l-k:
            return False
        sub1 = s[i-1:j]
        sub2 = s[k-1:l]
        cnt = 0
        for m in range(len(sub1)):
            if sub1[m] != sub2[m]:
                cnt += 1
                if cnt > 1:
                    return False
        return True

s = "abbaabbaab"
i, j, k, l = 1, 2, 9, 10
ans = Solution().almostEqualString(s, i, j, k, l)
print(ans)