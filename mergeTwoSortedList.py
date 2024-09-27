class Node:
    def __init__(self, data:int):
        self.val = data
        self.next = None
        
def printList(list):
    while list:
        print(list.val)
        list = list.next 
        
def mergeTwoSortedList(list1, list2):
    head = dummyNode = Node(0)
    while list1 and list2:
        if list1.val < list2.val:
            dummyNode.next = list1
            list1 = list1.next
        else:
            dummyNode.next = list2
            list2 = list2.next    
        dummyNode = dummyNode.next
    if list1:
        dummyNode.next = list1
    else:
        dummyNode.next = list2
        
    print("Final List : ", printList(dummyNode.next))
    return head.next 
    
if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(4)
    list1.next.next.next = Node(6)
    list1.next.next.next.next = Node(11)
    print("List1", printList(list1))

    list2 = Node(2)
    list2.next = Node(5)
    list2.next.next = Node(6)
    print("List2: ", printList(list2))
    
    printList(mergeTwoSortedList(list1, list2))    