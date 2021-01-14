# I have chellanged myself not to use isdigit() function of string

class Solution:
    def myAtoi(self, str: str) -> int:
        new = str.strip()
        if len(new)<1:
            return 0
        else:
            neg = False
            
            if new[0] == "-":
                neg = True
                string = new.replace("-","",1)
            elif new[0] == "+":
                string = new.replace("+", "",1)
            else:
                string = new
                
            num = 0
            k = 0
            length = len(string) -1
            
            for i, s in enumerate(string):
                j = length - i
                if s == ".":
                    k = k + length
                    break
                elif s == "1":
                    num = num+(1*10**j)
                elif s == "2":
                    num = num+(2*10**j)
                elif s == "3":
                    num = num+(3*10**j)
                elif s == "4":
                    num = num+(4*10**j)
                elif s == "5":
                    num = num+(5*10**j)
                elif s == "6":
                    num = num+(6*10**j)
                elif s == "7":
                    num = num+(7*10**j)
                elif s == "8":
                    num = num+(8*10**j)
                elif s == "9":
                    num = num+(9*10**j)
                elif s != "0":
                    k = len(string) - i
                    break
                    
            while (new[0] == "0"):
                new = new.replace("0","", 1)
                if len(new) < 1:
                    return 0
                    break

            if k>0:
                num = round(num/(10**k))
        
            if neg == True:
                num = 0-num
                
            if num < -2**31:
                num = -2**31
            
            if num > (2**31)-1:
                num = (2**31)-1
        
            return num    
