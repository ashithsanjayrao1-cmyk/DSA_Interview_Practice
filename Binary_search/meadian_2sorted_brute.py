class Solution():
    def medianBrute(self,arr1,arr2):

        n1 = len(arr1)
        n2 = len(arr2)
        arr3 = []


        i = 0
        j = 0

        while i < n1 and j <n2:
            if arr1[i] < arr2[j]:
                arr3.append(arr1[i])
                i += 1

            else:
                arr3.append(arr2[j])
                j += 1

        while i<n1:
            arr3.append(arr1[i])

            i+=1

        while j<n2:
            arr3.append(arr2[j])

            j +=1

        n = n1+n2 

        if n % 2 == 1:
            return float(arr3[n//2])

        else:
            return (arr3[n//2] + arr3[(n//2)-1])/2.0

s1 = Solution()

arr1 = [1,3,4,7,10,12]

arr2 = [2,3,6,15]

print(s1.medianBrute(arr1,arr2))
