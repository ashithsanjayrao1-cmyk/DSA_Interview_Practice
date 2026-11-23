class Queue:
    def __init__(self):

        self.s1 = []
        self.s2 = []


    def push(self,x):

        while self.s1:

            top_element = self.s1.pop()
            self.s2.append(top_element)

        self.s1.append(x)

        while self.s2:

            top_element = self.s2.pop()
            self.s1.append(top_element)

    def pop(self):
        if not self.s1:
            return -1

        return self.s1.pop()


    def top(self):
        if not self.s1:
            return -1


        return self.s1[-1]


if __name__ == "__main__":
    q = Queue()
    
    # Let's trace this!
    q.push(10)  # s1 becomes [10]
    q.push(20)  # 10 pours to s2. 20 goes in s1. 10 pours back on top. s1 becomes [20, 10]
    q.push(30)  # 10, 20 pour to s2. 30 goes in s1. 20, 10 pour back. s1 becomes [30, 20, 10]
    
    print(f"Top element: {q.top()}")   # Output: 10 (The oldest item, perfectly mimicking a Queue!)
    print(f"Popped: {q.pop()}")        # Output: 10
    print(f"New top: {q.top()}")