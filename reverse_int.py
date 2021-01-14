# using string
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if '-' in s:
            s = s.replace("-","")
        ans = [None]*len(s)
        i = len(s)
        for j in map(int, s):
            ans[i-1] = j
            i-=1
        ans = int(''.join(str(i) for i in ans))
        if ans > 2**31:
            return 0
        else:
            if x < 0:
                ans = 0 - ans
            return ans
        
