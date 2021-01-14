class Solution:
    def myPow(self, x: float, n: int) -> float: 
        if n == 0:
            return 1       
        elif ((abs(x) < 0.001) & (abs(n) > 6)) | ((n < -1000) & (abs(x) != 1)):
            return 0
        elif (abs(x) == 1):          
            if (n < 0) & (x < 0):
                x = abs(x)
            return x
        else:
            if n < 0:
                x = 1/x
            answer = x
            for i in range(abs(n)-1):
                answer = answer * x
            return answer
            
