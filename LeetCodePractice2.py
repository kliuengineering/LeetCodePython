"""
1. define the problem
2. gather information
3. analyze the problem
4. generate possible solution
5. evaluate solutions.
6. choose the best solution
7. implement solution.

Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



head <- 1 -> 2 -> 3 -> 4 -> nullptr              
        |    |
      prev curr

next = curr.next
curr.next = prev
prev = curr
curr = next

Time: O(n)
Space: O(1)

1<-2<-3<-4


Constraints:

The number of nodes in the list is the range [0, 5000].

-5000 <= Node.val <= 5000

"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      """
      		Decompose the question:
           1. how to change the links between the node so that its backward.
           2. how to keep track of the new head
           
           
           Possible solution:
           1. l, r.
           2. 
           
          
      """
      
        curr = head
        prev = None
        3.next.next = 3
        2.next.next= 2
        
        
        1-2-3-
        
      
      # recursive solution
      # goal
      	# base case: return when there is no more node
        # recursive step:
        	# keeps traversing
          # keeps swapping
          
        if curr == None:
          return prev
        else:
          next = curr.next
          curr.next = prev
          prev = curr
          curr = next
          reverseList(curr)