# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1. Initialize both 'slow' and 'fast' pointers to the 'head' of the linked list
    2. Move the 'fast' pointer by two steps for every one step 'slow' takes
    3. By moving at different speeds, 'fast' reaches the end by the time 'slow' in at the middle
    4. Return the node pointed to by 'slow'
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

