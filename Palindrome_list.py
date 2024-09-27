class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        
def printList(list:Node):
    while list:
        print(list.val)
        list = list.next

def isPalindrome(head: Node) -> bool:
    # Middle of a linked list 
    slow = fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next
    
    # Reverse second half of a list
    prev = None    
    while slow:
        next = slow.next
        slow.next = prev
        prev = slow 
        slow = next
    
    # check for palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False 
        left = left.next 
        right = right.next
    return True
    
    
    
if __name__== "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    print("Head :: ", printList(head))
    print("After printing head")
    print("Palindrome : ", isPalindrome(head))
        
        
    
    
    