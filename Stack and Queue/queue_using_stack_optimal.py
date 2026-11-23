class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self,x):

        self.s1.append(x)

    def pop(self):

        if self.s2:

            return self.s2.pop()
        else:

            while self.s1:

                top_element = self.s1[-1]
                self.s2.append(top_element)

                self.s1.pop()

            return self.s2.pop()

    def top(self):

        if self.s2:
            return self.s2[-1]
        else:

            while self.s1:

                top_element = self.s1[-1]
                self.s2.append(top_element)

                self.s1.pop()

            return self.s2[-1]


if __name__ == "__main__":
    q = Queue()
    
    q.push(10)
    q.push(20)
    
    print(f"Top: {q.top()}")  # Output: 10
    print(f"Pop: {q.pop()}")  # Output: 10