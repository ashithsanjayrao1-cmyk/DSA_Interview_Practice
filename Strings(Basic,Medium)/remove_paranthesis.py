class Solution():
    def removeParanthseis(self,s: str) -> str:
        result = []

        depth = 0

        for char in s:
            if char == '(':
                if depth>0:
                    result.append(char)
                depth += 1

            elif char == ')':
                depth -= 1

                if depth > 0:
                    result.append(char)

        return "".join(result)

s1 = Solution()
s = "(()())(())"
print(s1.removeParanthseis(s))