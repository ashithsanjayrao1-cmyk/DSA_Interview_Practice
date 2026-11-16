class Solution():
    def intersection(self,arr1,arr2):

        n1 = len(arr1)
        n2 = len(arr2)

        ans = []

        i = 0
        j = 0

        while i < n1 and j<n2:
                
                if arr1[i] == arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                    j += 1

                elif arr1[i] < arr2[j]:
                    i += 1
                else:
                    j += 1
        return ans

s1 = Solution()

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5,6]

print(s1.intersection(arr1,arr2))




#         n1 = len(arr1)
#         n2 = len(arr2)

#         vis = [0] * (n2)

#         ans = []


#         for i in range(n1):

#             for j in range(n2):

#                 if arr1[i] == arr2[j] and vis[j] ==0:

#                     ans.append(arr1[i])

#                     vis[j] = 1
#                     break

#                 if arr2[j] > arr1[i]:
#                     break

#         return ans
# s1 = Solution()

# arr1 = [1,2,3,4,5,6,7]
# arr2 = [1,2,3,4,5,6]

# print(s1.intersection(arr1,arr2))



