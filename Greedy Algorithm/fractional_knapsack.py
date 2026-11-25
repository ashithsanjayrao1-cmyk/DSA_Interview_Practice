class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight

class Solution():
    def fractionalKnapSack(self,W,arr):

        arr.sort(key = lambda x: x.value / x.weight , reverse = True)

        n = len(arr)

        total_val = 0.0

        for i in range(n):

            if arr[i].weight <= W:
                total_val += arr[i].value

                W-= arr[i].weight

            else:
                total_val += (arr[i].value/arr[i].weight) * W

                break

        return total_val


if __name__ == "__main__":
    # Create 3 items: (Value, Weight)
    item1 = Item(100, 20)   # Ratio: 6
    item2 = Item(60, 10)  # Ratio: 5
    item3 = Item(100, 50)  # Ratio: 4
    item4 = Item(200,50)
    arr = [item1, item2, item3, item4]
    
    # Knapsack weight capacity is 50
    W = 90
    
    s = Solution()
    print(f"Maximum value in knapsack: {s.fractionalKnapSack(W, arr)}")