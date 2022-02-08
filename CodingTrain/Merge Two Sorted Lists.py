# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		#create dummy node so we can compare the first node in each list
		dummy = ListNode()

		#initialise current node pointer
		curr = dummy

		#while the lists are valid
		while list1 and list2:

			#if the value is list1 is less than the value in list2
			if list1.val < list2.val:

				#the next node in the list will be the list1 node
				curr.next = list1
				list1 = list1.next

			else:

				#if not then the next node in the list will be the list2 node
				curr.next = list2
				list2 = list2.next

			#increment node
			curr = curr.next

		#if list1 node is valid but not list2 node add the rest of the nodes from list1
		if list1:
			curr.next = list1

		#if list2 node is valid but not list1 node add the rest of the nodes from list2
		elif list2:
			curr.next = list2

		#return the head of the merged list
		return dummy.next