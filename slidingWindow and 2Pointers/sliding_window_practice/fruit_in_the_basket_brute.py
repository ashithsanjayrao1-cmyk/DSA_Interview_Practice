class Solution():
    def fruitInaBasket(self,arr):
        n = len(arr)
        max_len = 0
        for i in range(n):
            basket = set()

            for j in range(i,n):
                basket.add(arr[j])
                if len(basket) <= 2:
                    length = j-i+1

                    max_len = max(length,max_len)

        return max_len
s1 = Solution()
print(s1.fruitInaBasket([1,3,2,2,2]))