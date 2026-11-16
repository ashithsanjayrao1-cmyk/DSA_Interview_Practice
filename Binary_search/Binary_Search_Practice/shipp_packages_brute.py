class Solution():
    def func(self,weight,capacity):
        n = len(weight)

        count = 0

        day = 1

        for i in range(n):

            if count + weight[i] > capacity:

                day += 1
                count = weight[i]

            else:

                count+= weight[i]

        return day


    def shipload(self,weight,days):

        max_len = max(weight)

        total_sum = sum(weight)

        for i in range(max_len,total_sum+1):

            curr_day = self.func(weight,i)

            if curr_day <= days:
                return i
            
s1 = Solution()

print(s1.shipload([1,2,3,4,5,6,7,8,9,10],5))




