class Node:

    def __init__(self,data,next_node = None):

        self.data = data
        self.next = next_node

def arr_to_linked_list(arr):
    n = len(arr)

    if not arr:
        return None


    head = Node(arr[0])

    mover = head

    for i in range(1,n):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head

def getLength(head):

    count = 0
    temp = head

    while temp is not None:
        count += 1

        temp = temp.next


    return count



def print_linked_list(head):
    temp = head

    while temp is not None:

        print(temp.data,end="-> ")
        temp = temp.next

    print("None")

arr = [12,5,8,7]

head = arr_to_linked_list(arr)

length = getLength(head)

print_linked_list(head)


print(length)


