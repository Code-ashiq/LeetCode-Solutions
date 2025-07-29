#problem 83. Remove Duplicates from Sorted List, Level: Easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # Initialize the current node to the head of the linked list
        curr = head

         # Traverse the list until the end
        while curr and curr.next:
            # If the current node's value is the same as the next node's value
            if curr.val == curr.next.val:
                # Skip the next node by pointing current's next to the next's next
                # This removes the duplicate node from the list
                curr.next = curr.next.next
            else:
                 # Move to the next node if no duplicate
                curr = curr.next
        # Return the updated head of the list with duplicates removed
        return head
