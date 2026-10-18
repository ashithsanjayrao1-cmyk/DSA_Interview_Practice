class Solutiion():
    def findDays(self,weights,capacity):
        days = 1
        current_load = 0

        for weight in weights:

            if weight + current_load > capacity:
                days += 1
                current_load = weight

            else:
                current_load += weight

        return days


    def binarysearch(self,weight,days):

        low = max(weight)
        high = sum(weight)

        while low<= high:
            mid = (low+high)//2
 
            no_of_days = self.findDays(weight,mid)
            if no_of_days <= days:
                high = mid-1

            else:
                low = mid+1

        return low


s1 = Solutiion()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5 


print(s1.binarysearch(weights,days))