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

def deleteOccurence(head,key):
    temp = head

    while temp is not None:

        if temp.data == key:
            if temp == head:
                head= head.next

            next_node = temp.next
            prev_node = temp.prev

            if next_node:
                next_node.prev = prev_node

            if prev_node:
                prev_node.next = next_node

            temp = temp.next

        else:

            temp = temp.next

    return head




def print_doubly_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")


arr = [10,4,10,10,6,10]
head = arr_to_doubly_linked_list(arr)
head = deleteOccurence(head,10)
print_doubly_linked_list(head)
