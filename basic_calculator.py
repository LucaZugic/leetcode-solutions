class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        res = 0
        stack = []
        new = s.replace(" ","")
        for i in range(len(new)):
            val = new[i]
            if val.isdigit():
                num = num*10 + int(val)
            elif val in '-+':
                res += num*sign
                sign = -1 if val == '-' else 1
                num = 0
            elif val == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif val == ")":
                res +=sign*num
                res *=stack.pop()
                res +=stack.pop()
                num = 0
        return res + num*sign
