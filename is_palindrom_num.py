# without using string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            if x < 10:
                return True
            else:
                i = 0
                x2 = x
                while x2 > 0:
                    x2 = x2//10
                    i+=1
                stack1 = [None]*(i-1) +[x%10]
                k = i
                for j in range(1, i):
                    stack1[k-2] = (round(x//(10**j))%10)
                    k -= 1
                stack2 = [None]*(i//2)
                for ii in range(i//2):
                    if stack1[ii] == stack1[-(ii+1)]:
                        stack2[ii] = True
                    else:
                        stack2[ii] = False
                if False in stack2:
                    return False
                else:
                    return True
                    
