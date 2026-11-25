class Solution():
    def lemonadeChange(self,arr):
        n = len(arr)
        five = 0 
        ten = 0
        twenty = 0

        for i in range(n):
            if arr[i] == 5:
                five+=1
            elif arr[i] == 10:
                if five:
                    five-=1
                    ten+=1
                else:
                    return False
                
            else:

                if ten and five:

                    twenty+=1
                    five-=1
                    ten-=1

                elif five >= 3:
                    twenty +=1
                    five-=3

                else:
                    return False
        return True
s1 = Solution()
print(s1.lemonadeChange([5,5,5,10,20]))