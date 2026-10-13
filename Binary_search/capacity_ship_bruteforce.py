class Solution():
    def findDays(self,weights,capacity):
        days = 1
        current_load = 0

        for weight in weights:

            if current_load + weight > capacity:
                days += 1
                current_load = weight

            else:
                current_load += weight

        return days

    def shiWeight(self,weights,days):

        min_cap = max(weights)

        max_cap = sum(weights)

        for cap in range(min_cap,max_cap+1):
            if self.findDays(weights,cap) <= days:
                return cap

        return -1

s1 = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5 

print(s1.shiWeight(weights,days))