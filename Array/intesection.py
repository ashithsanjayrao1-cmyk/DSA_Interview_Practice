class Solution():
    def intersection(self,arr1,arr2):

        n1 = len(arr1)
        n2 = len(arr2)

        i = 0
        j = 0


        ans = []

        while i < n1  and j < n2:

            if arr1[i] < arr2[j]:
                i += 1

            elif arr2[j] <  arr1[i]:
                j += 1


            else:
                ans.append(arr1[i])
                j +=1
                i+=1

        return ans
    




        # visited_arr = [0] * n2

        # for i in range(n1):

        #     for j in range(n2):
        #         if arr1[i] == arr2[j] and visited_arr[j] == 0:
        #             ans.append(arr1[i])
        #             visited_arr[j] = 1
        #             break

        #         elif arr2[j] > arr1[i]:
        #             break

        # return ans

s1 = Solution()

arr1 = [1,2,2,3,3,4,5,6]

arr2 = [2,3,3,5,6,6,7]

print(s1.intersection(arr1,arr2))


