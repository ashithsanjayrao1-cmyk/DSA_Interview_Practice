from collections import deque

class Stack:

    def __init__(self):

        self.q = deque()

    def push(self,x):

        s = len(self.q)

        self.q.append(x)


        for _ in range(s):

            front_element = self.q[0]
            self.q.append(front_element)


    def pop(self):

        if not self.q:
            return -1

        return self.q.popleft()

    def top(self):
        if not self.q:
            return -1

        return self.q[0]

if __name__ == "__main__":
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    
    print(f"Top element: {st.top()}")   # Output: 30
    print(f"Popped: {st.pop()}")        # Output: 30
    print(f"New top: {st.top()}")