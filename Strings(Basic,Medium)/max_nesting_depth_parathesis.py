class Solution():
    def MaxDepth(self,s:str) -> int:

        curreent_depth = 0
        max_depth = 0

        for char in s:
            if char == '(':
                curreent_depth += 1

            if curreent_depth > max_depth:
                max_depth = curreent_depth


            elif char == ')':
                curreent_depth -=1

        return max_depth

s1 = Solution()
s = "(1+(2*3)+((8)/4))+1"

print(s1.MaxDepth(s))