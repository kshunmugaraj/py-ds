"""
Reorder list

Input: 1->2->3->4
Output : 1->4->2->3

"""

class Node:
    def __init__(self, val: int , next=None):
        self.data = val
        self.next = next
    
def printList(head):
    while head:
        print(head.data)
        head = head.next
        
def reOrderList(head):
    # find the middle node
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        
    print("Second :", slow.next.data)
    # Reverse a list
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next 
        second.next = prev
        prev=second 
        second = tmp
     
    print("First , Second :", head.data, prev.data)   
    #Reorder a list
    first, second = head, prev
    while second:
        temp1, temp2 = first.next , second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
printList(head)
reOrderList(head)
printList(head)
    
    