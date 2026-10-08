class Solution():
    def majorityElementOptimal(self,arr):

        cnt1 = 0
        cnt2 = 0

        el1 = float('-inf')
        el2 = float('-inf')

        for num in arr:
            if cnt1 == 0 and num != el2:
                cnt1 = 1
                el1 = num

            elif cnt2 == 0 and num != el1:
                cnt2 = 1
                el2 = num

            elif num == el1:
                cnt1 +=1

            elif num == el2:
                cnt2 += 1

            else:

                cnt1 -= 1
                cnt2 -= 1
        ans = []
        count1 = 0
        count2 = 0
        threshold = len(arr) // 3


        for num in arr:
            if num == el1:
                count1 += 1
            elif num == el2:
                count2 += 1
                
        if count1 > threshold:
            ans.append(el1)
        if count2 > threshold:
            ans.append(el2)
            
        return ans
s1 = Solution()
arr = [11, 33, 33, 11, 33, 11]
print(s1.majorityElementOptimal(arr))
