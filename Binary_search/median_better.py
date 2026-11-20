class Solution():
    def median(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        n = n1 + n2

        index2 = n//2
        index1 = index2-1

        count = 0

        ind1 = -1
        ind2 = -1

        i = 0
        j = 0

        while i < n1 and j<n2:
            if arr1[i] < arr2[j]:
                if count == index1:
                 ind1 = arr1[i]

                if count == index2:
                    ind2 = arr1[i]

                count += 1

                i+=1
            else:
                if count == index1:
                    ind1 = arr2[j]

                if count == index2:
                    ind2 = arr2[j]

                count += 1
                j += 1
        
        while i< n1:
                if count == index1:
                    ind1 = arr1[i]
            
                if count == index2:
                    ind2 = arr1[i]
            
                count += 1
            
                i+=1

        while j < n2:
            if count == index1:
                ind1 = arr2[j]
            
            if count == index2:
                ind2 = arr2[j]
            
            count += 1
            j += 1

        if n % 2 == 1:
            return float(ind2)

        else:

            return (ind1+ind2)/2.0

s1 = Solution()
print(s1.median([1,3,5,7,9,11],[2,4,6,8]))

print(s1.median([1,3,4],[2,3]))


        