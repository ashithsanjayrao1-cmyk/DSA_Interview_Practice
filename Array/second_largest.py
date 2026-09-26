# class Solution():
#     def secondLar(self,arr):
#         n = len(arr)

#         if n < 2:
#             return -1

#         arr.sort()


#         largest = arr[-1]

#         for i in range(n-2,-1,-1):

#             if arr[i] != largest:
#                 return arr[i]


#         return -1


# s1 = Solution()

# arr = [1,4,4,6,2,11,27,27,27,27]


# print(s1.secondLar(arr))


class Solution():
    #def secondLar(self,arr):
        # n = len(arr)

        # largest = arr[0]
        # slargest = -1

        # for i in range(n):
        #     if arr[i] > largest:
        #         largest = arr[i]


        # for i in range(n):
        #     if arr[i] > slargest and arr[i] != largest:
        #             slargest = arr[i]


        # return slargest

    def SecondLar(self,arr):
        n =len(arr)

        largest = arr[0]
        slargest = -1

        for i in range(n):
            if arr[i] > largest:
                slargest = largest

                largest = arr[i]


            elif arr[i] < largest and arr[i] > slargest:

                slargest = arr[i]

        return slargest


                       

            




s2 = Solution()

arr = [5,9,7,8,10,10]

print(s2.SecondLar(arr))




    