class Solution():
    def majorityElement(self,arr):
         
         n = len(arr)

         ans = []

         mpp = {}

         threshold = n // 3

         for num in arr:
              mpp[num] = mpp.get(num,0) + 1

              if mpp[num] == threshold + 1:
                   
                   ans.append(num)

              if len(ans) == 2:
                   break


         return ans

s1 = Solution()
arr = [11, 33, 33, 11, 33, 11]
print(s1.majorityElement(arr))