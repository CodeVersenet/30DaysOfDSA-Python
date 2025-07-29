# Problem 278- First Bad Version
# The isBadVersion API is already defined for you.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
    
 # problem 141- Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False