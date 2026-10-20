class Solution():
    def totalFruit(self,fruits: list[int]) -> int:

        n = len(fruits)

        max_len = 0

        for i in range(n):

            basket = set()

            for j in range(i,n):

                basket.add(fruits[j])

                if len(basket) <= 2:
                    length = j-i+1

                    max_len = max(max_len,length)


                else:

                    break

        return max_len

s1 = Solution()
fruits = [1, 2, 1, 2, 3]
print(s1.totalFruit(fruits))   