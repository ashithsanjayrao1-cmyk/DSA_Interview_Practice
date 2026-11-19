class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

class Stack:

    def __init__(self):

        self.top_node = None
        self.curr_size = 0

    def push(self,x):
        temp = Node(x)

        temp.next = self.top_node
        self.top_node = temp
        self.curr_size += 1

    def pop(self):
        if self.top_node is None:
            return -1

        temp = self.top_node
        poped_value = temp.data
        self.top_node = self.top_node.next

        self.curr_size -= 1

        return poped_value

    def top(self):

        if self.top_node is None:
            return -1

        return self.top_node.data

    def size(self):
        return self.curr_size

if __name__ == "__main__":
    st = Stack()
    st.push(10)
    st.push(20)
    
    print(f"Top element: {st.top()}")   # Output: 20
    print(f"Stack size: {st.size()}")   # Output: 2
    
    print(f"Popped: {st.pop()}")        # Output: 20
    print(f"New top: {st.top()}")