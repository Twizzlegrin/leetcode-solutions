# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1. Initialize 'fast' and 'slow' pointers
    2. Move the 'fast' pointe rn steps forward
    3. Move both 'fast' and 'slow' until 'fast' reaches end
    4. Slow now points to node before the one to be removed
    5. Update 'next' reference of the 'slow' pointer to skip next node
    6. Return modified linked list
    """
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)  # Create a dummy node to handle edge cases
        dummy.next = head

        fast = slow = dummy

        # Move the fast pointer N steps forward
        for _ in range(n):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the Nth node by updating the next reference of the slow pointer
        slow.next = slow.next.next

        return dummy.next  # Return the modified linked list