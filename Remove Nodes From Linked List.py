# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        #Traversing the list
        while curr != None:
            while stack and (stack[-1].val < curr.val): #popping smaller values from the stack
                stack.pop()
            stack.append(curr)
            curr = curr.next
        dummy = ListNode(0)
        node = dummy
        # Rebuilding list
        for n in stack:
            node.next = n
            node = node.next
        node.next = None

        return dummy.next

            
