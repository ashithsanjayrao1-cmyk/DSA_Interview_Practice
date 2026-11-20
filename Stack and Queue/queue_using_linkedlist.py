class Node:
    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node
class Queue:
    def __init__(self):

        self.start = None
        self.end = None
        self.curr_size = 0

    def push(self,x):
        temp = Node(x)

        if self.start == None:
            self.start = temp 

            self.end = temp 

        else:
            self.end.next = temp

            self.end = temp
        self.curr_size += 1

    def pop(self):
        if self.start is None:
            print("Queue is empty")
            return -1
        temp = self.start
        popped_value = temp.data
        self.start = self.start.next
        self.curr_size -= 1

        return popped_value

    def top(self):
        if self.start is None:
            print("Que is Emplty")
            return -1

        return self.start.data
    def size(self):
        return self.curr_size

if __name__ == "__main__":
    q = Queue()
    q.push(10)
    q.push(20)
    
    print(f"Top element: {q.top()}")   # Output: 10
    print(f"Queue size: {q.size()}")   # Output: 2
    
    print(f"Popped: {q.pop()}")        # Output: 10
    print(f"New top: {q.top()}")