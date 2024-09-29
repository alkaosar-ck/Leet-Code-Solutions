from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_LinkedList(head):
    previous = None
    current = head
    
    while current:
        next_node = current.next 
        current.next = previous 
        previous = current  
        current = next_node  
    return previous  

def get(head):
    element = []
    current = head
    while current:
        element.append(str(current.val))
        current = current.next
    return element



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reversed = reverse_LinkedList(l1)
        l2_reversed = reverse_LinkedList(l2)
        
        num1 = ''.join(get(l1_reversed))
        num2 = ''.join(get(l2_reversed))
        
        total = int(num1) + int(num2)
        
        dummy_head = ListNode(0)
        current = dummy_head
        
        for digit in str(total)[::-1]: 
            current.next = ListNode(int(digit))
            current = current.next
        
        return dummy_head.next 