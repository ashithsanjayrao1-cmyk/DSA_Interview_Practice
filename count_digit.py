class Solution:

    def count_d(self,n):

        count = 0

        while(n>0):
            count +=1

            n = n //10

        return count

s1 = Solution()

n = 555


print(s1.count_d(n))


