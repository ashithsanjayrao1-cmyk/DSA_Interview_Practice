class Stack:


    def __init__(self):
        self.top = -1
        self.st = [0] * 10


    def push(self,x):
        self.top = self.top + 1
        self.st[self.top] = x

    def pop(self):
        self.top = self.top-1

    def get_top(self):
        return self.st[self.top]

    def size(self):

        return self.top+1

st = Stack()

print("Pushing 6, 3, 7...")
st.push(6)
st.push(3)
st.push(7)

print(f"Top element is: {st.get_top()}")
print(f"Size of stack is: {st.size()}")

print("\nPopping one element...")
st.pop()

print(f"Top element after pop is: {st.get_top()}")
print(f"Size after pop is: {st.size()}")

    