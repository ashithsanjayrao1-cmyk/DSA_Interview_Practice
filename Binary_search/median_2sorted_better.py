class Solution():
    def findMedianSortedBetter(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        n = n1+n2

        ind2 = n//2
        ind1 = ind2-1

        ind1_element = -1
        ind2_element = -1

        count = 0
        i = 0
        j = 0

        while i<n1 and j<n2:
            if arr1[i] < arr2[j]:
                if count == ind1:
                    ind1_element = arr1[i]

                if count == ind2:
                    ind1_element = arr1[i]

                count+=1
                i+=1

            else:
                if count == ind1:
                    ind1_element = arr2[j]
                if count == ind2:
                    ind2_element = arr2[j]
                count +=1
                j+=1


        while i<n1:

            if count == ind1:
                ind1_element = arr1[i]
            if count == ind2:
                ind2_element = arr1[i]
            count += 1
            i += 1

        while j<n2:
            if count == ind1:
                ind1_element = arr2[j]
            if count == ind2:
                ind2_element = arr2[j]
            count +=1
            j +=1

        if n % 2 == 1:
            return float(ind2_element)

        else:
            return (ind1_element + ind2_element) / 2.0

s1 = Solution()
arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

print(s1.findMedianSortedBetter(arr1,arr2))


