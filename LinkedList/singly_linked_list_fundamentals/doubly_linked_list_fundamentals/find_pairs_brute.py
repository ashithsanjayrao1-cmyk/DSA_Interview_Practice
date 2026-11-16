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


def findPairs(head,sum):
    temp1 = head
    ls = []

    while temp1 is not None:
        temp2 = temp1.next

        while temp2 is not None:
            if temp1.data + temp2.data == sum:
                ls.append((temp1.data,temp2.data))

            temp2 = temp2.next

        temp1 = temp1.next


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
