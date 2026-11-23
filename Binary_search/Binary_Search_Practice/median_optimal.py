class Solution():
    def medianOptimal(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        if n1 > n2:
            return self.medianOptimal(arr2,arr1)

        low = 0
        high = n1

        left_partiton = (n1+n2+1)//2

        n = n1 + n2

        while low <= high:
            mid1 = (low+high)//2

            mid2 = left_partiton - mid1


            l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = arr2[mid2 - 1] if mid2 > 0 else float("-inf")
            r1 = arr1[mid1] if mid1 < n1 else float('inf')
            r2 = arr2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if n% 2 == 1:
                    return float(max(l1,l2))
                else:
                    return (max(l1,l2) + min(r1,r2))/2.0

            elif l1 > r2:
                high = mid1-1

            else:
                low = mid1 + 1 
s1 = Solution()
print(s1.medianOptimal([1,3,5,7,9,11],[2,4,6,8]))
