class Solution:
    def pattern2(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end = " ")

            print()

S1 = Solution()
n = 5

S1.pattern2(n)