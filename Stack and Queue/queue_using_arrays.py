class Queue:
    def __init__(self):

        self.max_size = 10
        self.queue = [0] * self.max_size
        self.curSiz = 0
        self.start = -1
        self.end = -1


    def push(self,x):
        if self.curSiz == self.max_size:
            print("Queue is full")

            return

        if self.curSiz == 0:
            self.start = 0
            self.end = 0

        else:

            self.end = (self.end+1) % self.max_size

        self.queue[self.end] = x
        self.curSiz += 1

    def pop(self):
        if self.curSiz == self.max_size:
            print("")


        if self.curSiz == 0:
            return -1

        el = self.queue[self.start]

        if self.curSiz == 1:
            self.start = -1
            self.end = -1

        else:

            self.start = (self.start+1) % self.max_size

        self.curSiz -= 1
        return el

    def top(self):
        if self.curSiz == 0:
            return -1

        return self.queue[self.start]

    def size(self):
        return self.curSiz

if __name__ == '__main__':
    q = Queue()

    q.push(10)
    q.push(20)

    print(f"Top element is: {q.top()}")   # Output: 10
    print(f"Queue size is: {q.size()}")   # Output: 2
    
    print(f"Popped: {q.pop()}")           # Output: 10
    print(f"New top is: {q.top()}")

    


        