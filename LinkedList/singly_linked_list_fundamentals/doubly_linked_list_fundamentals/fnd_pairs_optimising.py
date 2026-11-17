class Node:
    def __init__(self,data,next_node = None,prev = None):

        self.data = data
        self.next = next_node
        self.prev = prev


def arr_to_doubly_linked_list(arr):

    n = len(arr)

    if not arr:
        return None

    head = Node(arr[0])
    back = head

    for i in range(1,n):
        temp = Node(arr[i],None,back)
        back.next = temp
        back = temp

    return head

def findTail(head):
    temp = head

    while temp.next is not None:
        temp = temp.next

    return temp


def findPairs(head,sum):

    left = head
    right = findTail(head)
    ls = []

    while left.data < right.data: 
        if left.data+right.data == sum:
            ls.append((left.data,right.data))
            left = left.next
            right= right.prev


        elif left.data + right.data < sum:
            left = left.next

        else:
            right = right.prev

    return ls



def print_doubly_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end = " <-> ")

        temp = temp.next

    print("None")


arr = [1,2,3,4,9]

head = arr_to_doubly_linked_list(arr)

node_to_delete = head.next

target = 5

pairs = findPairs(head,target)

print(pairs)
