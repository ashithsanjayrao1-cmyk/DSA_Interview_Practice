class Node:
    def __init__(self,data,next_node = None,random_node = None):

        self.data = data
        self.next = next_node
        self.random = random_node
def arr_to_linked_list(arr):
    n = len(arr)
    if not arr:
        return None
    head = Node(arr[0])
    mover = head

    for i in range(1,n):
        temp = Node(arr[i],None)
        mover.next = temp
        mover = temp
    return head

def clone(head):
    temp = head

    if head is None:
        return head
    


    while temp is not None:
        copyNode = Node(temp.data)
        copyNode.next = temp.next
        temp.next = copyNode

        temp =temp.next.next

    temp = head

    while temp is not None:

        copyNode = temp.next
        if temp.random is not None:

            copyNode.random = temp.random.next
        else:
            copyNode.random = None


        temp = temp.next.next

    dummyNode = Node(-1)
    res = dummyNode
    temp = head

    while temp is not None:

        res.next = temp.next
        temp.next = temp.next.next

        res = res.next
        temp = temp.next

    return dummyNode.next

         
       
def print_cloned_list(head):
    temp = head
    while temp is not None:

        random_data = temp.random.data if temp.random else "None"
        print(f"Node: {temp.data}, Random points to: {random_data}")
        temp = temp.next

node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3

node3.next = node4
node4.next = node5

# Connect random pointers according to the image
node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

print("Original List:")
print_cloned_list(node1)

cloned_head = clone(node1)

print("\nCloned List (Brute Force Hash Map):")
print_cloned_list(cloned_head)


    
